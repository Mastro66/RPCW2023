import json

with open("dbMusica.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

ttl = """@prefix : <http://rpcw.di.uminho.pt/2024/dbMusica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/dbMusica/> .

<http://rpcw.di.uminho.pt/2024/dbMusica> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/dbMusica#temCurso
:temCurso rdf:type owl:ObjectProperty ;
                rdfs:domain :Aluno ;
                rdfs:range :Curso .
                <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#temInstrumento
:temInstrumento rdf:type owl:ObjectProperty ;
                rdfs:domain :Curso ;
                rdfs:range :Instrumento .
                <http://purl.org/dc/elements/1.1/creator> "fernas" .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/dbMusica#anoCurso
:anoCurso rdf:type owl:DatatypeProperty ;
          rdfs:domain :Aluno ;
          rdfs:range xsd:int .
          <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#dataNasc
:dataNasc rdf:type owl:DatatypeProperty ;
          rdfs:domain :Aluno ;
          rdfs:range xsd:string .
          <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#designacao
:designacao rdf:type owl:DatatypeProperty ;
            rdfs:domain :Curso ;
            rdfs:range xsd:string .
            <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#duracao
:duracao rdf:type owl:DatatypeProperty ;
         rdfs:domain :Curso ;
         rdfs:range xsd:int .
         <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#nomeAluno
:nomeAluno rdf:type owl:DatatypeProperty ;
           rdfs:domain :Aluno ;
           rdfs:range xsd:string .
           <http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#nomeInstrumento
:nomeInstrumento rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Instrumento ;
                 rdfs:range xsd:string .
                 <http://purl.org/dc/elements/1.1/creator> "fernas" .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/dbMusica#Aluno
:Aluno rdf:type owl:Class .
		<http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#Curso
:Curso rdf:type owl:Class .
		<http://purl.org/dc/elements/1.1/creator> "fernas" .


###  http://rpcw.di.uminho.pt/2024/dbMusica#Instrumento
:Instrumento rdf:type owl:Class .
		<http://purl.org/dc/elements/1.1/creator> "fernas" .


#################################################################
#    Individuals
#################################################################

"""
for instrumento in bd["instrumentos"]:
    instrumento["#text"] = instrumento["#text"].replace(" ", "_")
    ttl+=f"""

###  http://rpcw.di.uminho.pt/2024/musica#{instrumento["#text"]}
:{instrumento["#text"]} rdf:type owl:NamedIndividual ;
            :idinstrumento "{instrumento["id"]}" ;
           :instrumento "{instrumento["#text"]}" .
    """
    
for curso in bd["cursos"]:
    curso["instrumento"]["#text"] = curso["instrumento"]["#text"].replace(" ", "_")
    curso["designacao"] = curso["designacao"].replace(" ", "_")
    ttl+=f"""
    
###  http://rpcw.di.uminho.pt/2024/musica#{curso["id"]}
:{curso["id"]} rdf:type owl:NamedIndividual ;
     :ensinaIntrumento :{curso["instrumento"]["#text"]} ;
     :designacao "{curso["designacao"]}" ;
     :duracao {curso["duracao"]} ;
     :idCurso "{curso["id"]}" .


"""
  
    
for aluno in bd["alunos"]:
    aluno["nome"]=aluno["nome"].replace(" ", "_")
    aluno["instrumento"] = aluno["instrumento"].replace(" ", "_")
    ttl+=f"""
    
###  http://rpcw.di.uminho.pt/2024/musica#{aluno["id"]}
:{aluno["id"]} rdf:type owl:NamedIndividual ;
        :temCurso :{aluno["curso"]} ;
        :temInstrumento :{aluno["instrumento"]} ;
        :anoCurso {aluno["anoCurso"]} ;
        :dataNasc "{aluno["dataNasc"]}" ;
        :idAluno "{aluno["id"]}" ;
        :nome "{aluno["nome"]}" ."""

print(ttl)

# Salve o conteúdo TTL em um arquivo
with open("Musica.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")