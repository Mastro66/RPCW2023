import json

with open("mapa-virtual.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

ttl = """@prefix : <http://rpcw.di.uminho.pt/2024/mapa_virtual/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/mapa_virtual/> .

<http://rpcw.di.uminho.pt/2024/mapa_virtual> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#temDestino
:temDestino rdf:type owl:ObjectProperty ;
                rdfs:domain :Ligacao ;
                rdfs:range :Cidade .

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#temOrigem
:temOrigem rdf:type owl:ObjectProperty ;
                rdfs:domain :Ligacao ;
                rdfs:range :Cidade .
                
#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#idCidade
:idCidade rdf:type owl:DatatypeProperty ;
          rdfs:domain :Cidade ;
          rdfs:range xsd:string .
          
          
###  http://rpcw.di.uminho.pt/2024/mapa_virtual#idLigacao
:idLigacao rdf:type owl:DatatypeProperty ;
          rdfs:domain :Ligacao ;
          rdfs:range xsd:string .
          

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#nomeCidade
:nomeCidade rdf:type owl:DatatypeProperty ;
          	rdfs:domain :Cidade ;
          	rdfs:range xsd:string .
          

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#numPopulacao
:numPopulacao rdf:type owl:DatatypeProperty ;
              rdfs:domain :Cidade ;
        	  rdfs:range xsd:int .
            

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#temDescricao
:temDescricao rdf:type owl:DatatypeProperty ;
         	  rdfs:domain :Cidade ;
         	  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/mapa_virtual#idInstrumento
:nomeDistrito rdf:type owl:DatatypeProperty ;
              rdfs:domain :Cidade ;
              rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/mapa_virtual#temDistancia
:temDistancia rdf:type owl:DatatypeProperty ;
             rdfs:domain :Ligacao ;
             rdfs:range xsd:float .

#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#Cidade
:Cidade rdf:type owl:Class .
		

###  http://rpcw.di.uminho.pt/2024/mapa_virtual#Ligacao
:Ligacao rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

"""

for Cidade in bd["cidades"]:
        ttl += f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{Cidade["id"]}
:{Cidade["id"]} rdf:type owl:NamedIndividual ,
        :Cidade ;
        :idCidade "{Cidade["id"]}" ;
        :nomeCidade "{Cidade["nome"]}" ;
        :numPopulacao "{Cidade["população"]}" ;
        :temDescricao "{Cidade["descrição"]}" ;
        :nomeDistrito "{Cidade["distrito"]}" .
"""

for Ligacao in bd["ligações"]:
        ttl+=f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{Ligacao["id"]}
:{Ligacao["id"]} rdf:type owl:NamedIndividual ,
        :Ligacao ;
        :idLigacao "{Ligacao["id"]}" ;
        :temOrigem :{Ligacao["origem"]} ;
        :temDestino :{Ligacao["destino"]} ;
        :temDistancia "{Ligacao["distância"]}" .

"""
print(ttl)

# Salve o conteúdo TTL em um arquivo
with open("Mapa.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")