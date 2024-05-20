from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Carregar os dados dos alunos
with open('aval-alunos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    alunos = data['alunos']

# Função auxiliar para calcular a nota final
def calcular_nota_final(aluno):
    if aluno['projeto'] < 10:
        return 'R'
    
    notas_exames = [nota for key, nota in aluno['exames'].items() if nota is not None]
    if not notas_exames or max(notas_exames) < 10:
        return 'R'
    
    nota_tpc = sum(tp['nota'] for tp in aluno['tpc'])
    nota_final = nota_tpc + 0.4 * aluno['projeto'] + 0.4 * max(notas_exames)
    
    return nota_final if nota_final >= 10 else 'R'

@app.route('/api/alunos', methods=['GET'])
def get_alunos():
    curso = request.args.get('curso')
    group_by = request.args.get('groupBy')
    
    if curso:
        result = [aluno for aluno in alunos if aluno['curso'] == curso]
        result = sorted(result, key=lambda x: x['nome'])
    elif group_by == 'curso':
        cursos = {}
        for aluno in alunos:
            if aluno['curso'] not in cursos:
                cursos[aluno['curso']] = 0
            cursos[aluno['curso']] += 1
        result = [{'curso': curso, 'total': total} for curso, total in cursos.items()]
    elif group_by == 'projeto':
        projetos = {}
        for aluno in alunos:
            if aluno['projeto'] not in projetos:
                projetos[aluno['projeto']] = 0
            projetos[aluno['projeto']] += 1
        result = [{'projeto': projeto, 'total': total} for projeto, total in projetos.items()]
    elif group_by == 'recurso':
        result = [{'idAluno': aluno['idAluno'], 'nome': aluno['nome'], 'curso': aluno['curso'], 'recurso': aluno['exames'].get('recurso', None)} for aluno in alunos if 'recurso' in aluno['exames']]
        result = sorted(result, key=lambda x: x['nome'])
    else:
        result = sorted([{'idAluno': aluno['idAluno'], 'nome': aluno['nome'], 'curso': aluno['curso']} for aluno in alunos], key=lambda x: x['nome'])
    
    return jsonify(result)

@app.route('/api/alunos/<id>', methods=['GET'])
def get_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno['idAluno'] == id), None)
    return jsonify(aluno) if aluno else ('', 404)

@app.route('/api/alunos/tpc', methods=['GET'])
def get_alunos_tpc():
    result = [{'idAluno': aluno['idAluno'], 'nome': aluno['nome'], 'curso': aluno['curso'], 'tpcRealizados': len(aluno['tpc'])} for aluno in alunos]
    result = sorted(result, key=lambda x: x['nome'])
    return jsonify(result)

@app.route('/api/alunos/avaliados', methods=['GET'])
def get_alunos_avaliados():
    result = [{'idAluno': aluno['idAluno'], 'nome': aluno['nome'], 'curso': aluno['curso'], 'notaFinal': calcular_nota_final(aluno)} for aluno in alunos]
    result = sorted(result, key=lambda x: x['nome'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
