import xml.etree.ElementTree as ET

# Load the XML file
with open("biblia.xml", 'r') as f:
    bd = ET.parse(f)

root = bd.getroot()

# Dictionary to hold people and their genders
people = {}

# Initialize the TTL output string
ttl = """@prefix : <http://rpcw.di.uminho.pt/2024/familia/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/familia/> .

<http://rpcw.di.uminho.pt/2024/familia> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#temMae
:temMae rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa .


###  http://rpcw.di.uminho.pt/2024/familia#temPai
:temPai rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pessoa .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#Pessoa
:Pessoa rdf:type owl:Class .

"""

for person in root.iter('person'):
    # Create a dictionary of IDs and their respective sex for easy lookup
    people[person.find('id').text] = person.find('sex').text
    
for person in root.iter('person'):
    id = person.find('id').text
    name = person.find('namegiven').text if person.find('namegiven') is not None else 'Unknown'
    
    parents = person.findall('parent')
    mae, pai = "", ""
    
    for parent in parents:
        parent_id = parent.get('ref')
        # Determine gender from the stored dictionary
        if people.get(parent_id) == 'F':
            mae = parent_id
        else:
            pai = parent_id
    
    # RDF descriptions for each person
    register = f"""
###  http://rpcw.di.uminho.pt/2024/familia#{id}
:{id} rdf:type owl:NamedIndividual ,
              :Pessoa ;
        :nome "{name}" .\n"""
    if pai != "":
        register += f"    :{id} :temPai :{pai} .\n"
    if mae != "":
        register += f"    :{id} :temMae :{mae} .\n"
    
    # Append each person's information to the ttl string
    ttl += register

# Write the TTL data to a file
with open("familia.ttl", "w") as f:
    f.write(ttl)

print("TTL data has been written to familia.ttl.")
