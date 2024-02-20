# TPC1 - Mapeamento de Ontologia e Serialização RDF para Dados de Registo de Plantas

Este trabalho envolve a conversão de dados de registo de plantas de um formato JSON para uma ontologia RDF utilizando a serialização Turtle (TTL). A ontologia RDF resultante é projetada para representar informações sobre árvores (Arvores) e as suas propriedades associadas, como localização, espécie e detalhes de manutenção.

## Ficheiros:
[plantas.json](plantas.json): Ficheiro de entrada contendo dados de registo de plantas em formato JSON.

[Plantas.ttl](Plantas.ttl): Ficheiro de saída que armazena a ontologia RDF em serialização Turtle (TTL) (Obtido após corrermos o pyPlantas.py).

[pyPlantas.py](pyPlantas.py): Script em Python responsável pelo processo de conversão.

## Passos:

### 1. Leitura dos Dados JSON:

O script começa por ler os dados de registo de plantas a partir do ficheiro "[plantas.json](plantas.json)" utilizando o módulo JSON. 

Foi necessário abrir o ficheiro utilizando a função open com a especificação do formato UTF-8 (encoding="utf-8"). Esta medida serve para garantir que os dados contidos no ficheiro, codificados em UTF-8, fossem lidos corretamente durante o processo de carregamento com a função json.load(f).

```python
import json

with open("plantas.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise
```

### 2. Definição da Ontologia:

A ontologia Turtle (TTL) é definida utilizando várias _Classes_, _Object Properties_ e _Data Properties_. Estas incluem _Classes_ como "Arvore", _Object Properties_ como "plantadanaRua" (plantada na rua) e _Data Properties_ como "codigoDeRua" (Código de Rua).

### 3. _Individuals_:

Nesta seção, são apresentadas as instâncias individuais geradas durante o processo de mapeamento da ontologia. Cada instância representa uma entidade específica, como Rua, Local, Freguesia, Espécie, Nome Científico, Gestor e Implantação.

Cada instância é associada à sua classe correspondente e reflete as informações específicas presentes nos dados JSON, proporcionando uma representação semântica mais rica na ontologia RDF.

### 4. Guardar a Ontologia:

A ontologia resultante é guardada em formato Turtle no ficheiro "[Plantas.ttl](Plantas.ttl)".

```python
with open("Plantas.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")
```
## Ontologia - Definição

### _Classes_:
Arvore:
Representa o conceito de uma árvore.

Rua:
Representa o conceito de uma rua.

Local:
Representa o conceito de uma localização.

Freguesia:
Representa o conceito de uma freguesia.

Espécie:
Representa o conceito de uma espécie de árvore.

Nome Científico:
Representa o nome científico de uma árvore.

Gestor:
Representa o gestor ou responsável por uma árvore.

Implantação:
Representa a zona de implantação de uma árvore.

### _Object Properties_:

plantadanaRua (plantada na rua):
Relaciona uma árvore com uma rua.

plantadanoLocal (plantada na localização):
Relaciona uma árvore com uma localização.

plantadanaFreguesia (plantada na freguesia):
Relaciona uma árvore com uma freguesia.

pertenceAEspecie (pertence à espécie):
Especifica a espécie à qual uma árvore pertence.

temnomeCientifico (tem nome científico):
Especifica o nome científico de uma árvore.

temGestor (tem gestor):
Especifica o gestor ou responsável por uma árvore.

zonaImplantacao (zona de implantação):
Especifica a zona de implantação de uma árvore.

### _Data Properties_:
id: Representa o identificador único de uma árvore.

numeroDeRegisto (número de registo):
Representa o número de registo de uma árvore.

codigoDeRua (código da rua):
Representa o código da rua onde uma árvore está plantada.

numeroDeIntervencoes (número de intervenções):
Representa o número de intervenções numa árvore.

caldeira (caldeira):
Representa se uma árvore tem caldeira (booleano).

tutor:
Representa se uma árvore tem tutor (booleano).

dataDeAtualizacao (data de atualização):
Representa a data da última atualização de uma árvore.

estado (estado):
Representa o estado de uma árvore.

## Forma de Utilização:
1. Certificar que o ficheiro de entrada "[plantas.json](plantas.json)" está presente com os dados de registo de plantas necessários.
2. Executar o script [pyPlantas.py](pyPlantas.py)" para gerar a ontologia RDF em formato Turtle.
3. A ontologia resultante é guardada no ficheiro "[Plantas.ttl](Plantas.ttl)".

## Autor
👤 **Fernando Alves - PG54470**
