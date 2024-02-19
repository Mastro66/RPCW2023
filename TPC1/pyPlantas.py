import json

with open("plantas.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

ttl = f"""@prefix : <http://rpcw.di.uminho.pt/2024/plantas/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/plantas/> .

<http://rpcw.di.uminho.pt/2024/plantas> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .

#################################################################
#    Classes - Completo
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/plantas#Arvore
:Arvore rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Rua
:Rua rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Local
:Local rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Freguesia
:Freguesia rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Especie
:Espécie rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#NomeCientífico
:Nome_Científico rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Gestor
:Gestor rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#Implantação
:Implantação rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

#################################################################
#    Object Properties - Completo
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/plantas#plantadanaRua
:plantadanaRua rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Rua ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#plantadanoLocal
:plantadanoLocal rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Local ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#plantadanaFreguesia
:plantadanaFreguesia rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Freguesia ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#pertencaAEspecie
:pertenceAEspecie rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Espécie ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#temnomeCientifico
:temnomeCientifico rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Nome Científico ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#temGestor
:temGestor rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Gestor ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

###  http://www.rpcw.di.uminho.pt/2024/plantas#zonaImplantacao
:zonaImplantacao rdf:type owl:ObjectProperty ;
          rdfs:domain :Arvore ;
          rdfs:range :Implantação ;
          <http://purl.org/dc/elements/1.1/creator> "fernas" .

#################################################################
#    Data properties - Arranjado 
#################################################################

<http://www.rpcw.di.uminho.pt/2024/plantas#id> 
:id rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:int ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#numeroDeRegisto> 
:numeroDeRegisto rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:int ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#codigoDeRua> 
:codigoDeRua rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:int ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#numeroDeIntervencoes> 
:numeroDeIntervencoes rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:int ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#caldeira> 
:caldeira rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:boolean ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#tutor> 
:tutor rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:boolean ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#dataDeAtualizacao> 
:dataDeAtualizacao rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:dateTime ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .

<http://www.rpcw.di.uminho.pt/2024/plantas#estado> 
:estado rdf:type owl:DatatypeProperty ;
        rdfs:domain :Arvore ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "fernas" .
"""


for planta in bd:
    registo = f"""
###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}
<http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                    :Arvore ;
                                                    :id "{planta['Id']}"^^xsd:int ;
                                                    :numeroDeRegisto "{planta['Número de Registo']}"^^xsd:int ;
                                                    :codigoDeRua "{planta['Código de rua']}"^^xsd:int ;
                                                    :plantadanaRua "{planta['Rua'].replace(" ", "_")}^^xsd:string ;
                                                    :plantadanoLocal "{planta['Local'].replace(" ", "_")}^^xsd:string ;
                                                    :plantadanaFreguesia "{planta['Freguesia'].replace(" ", "_")}^^xsd:string ;
                                                    :pertenceAEspecie "{planta['Espécie'].replace(" ", "_")}^^xsd:string ;
                                                    :temnomeCientifico "{planta['Nome Científico'].replace(" ", "_")}^^xsd:string ;
                                                    :estado "{planta['Estado']}"^^xsd:string ;
                                                    :caldeira "{planta['Caldeira']}"^^xsd:boolean ;
                                                    :tutor "{planta['Tutor']}"^^xsd:boolean ;
                                                    :zonaImplantacao "{planta['Implantação'].replace(" ", "_")}"^^xsd:string ;
                                                    :temGestor "{planta['Gestor']}"^^xsd:string ;
                                                    :dataDeAtualizacao "{planta['Data de actualização']}"^^xsd:dateTime ;
                                                    :numeroDeIntervencoes "{planta['Número de intervenções']}"^^xsd:int .

#################################################################
#    Individuals - Arranjado
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Rua'].replace(" ", "_")}
:{planta['Rua'].replace(" ", "_")} rdf:type owl:NamedIndividual , 
                :Rua .
                
###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ", "_")}
:{planta['Local'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                :Local .
                
###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Freguesia'].replace(" ", "_")}
:{planta['Freguesia'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                :Freguesia .
                
###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Espécie'].replace(" ", "_")}
:{planta['Espécie'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                :Espécie .

###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Nome Científico'].replace(" ", "_")}
:{planta['Nome Científico'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                :Nome Científico .

###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Gestor']}
:{planta['Gestor']} rdf:type owl:NamedIndividual ,
                :Gestor .

###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Implantação'].replace(" ", "_")}
:{planta['Implantação'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                :Implantação .


"""
    ttl += registo

# Salve o conteúdo TTL em um arquivo
with open("Plantas.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")
