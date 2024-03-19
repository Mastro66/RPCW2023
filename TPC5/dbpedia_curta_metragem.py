import json
import requests

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT ?movie ?title WHERE {
 	?movie dbo:runtime ?duration .
 	FILTER (?duration < 60)
 	?movie rdfs:label ?title .
 	FILTER (LANG(?title) = 'en') .
}
"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": sparql_query,
    "format": "json"
}

# Send the SPARQL query using requests
response = requests.get(sparql_endpoint, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    # Print the results
    filmes = []
    for result in results["results"]["bindings"]:
        filme = {}
        filme['uri'] = result["movie"]["value"]
        filme['nome'] = result["title"]["value"]
        filmes.append(filme)
        
    with open('curta_metragem.json', 'w') as outfile:
        json.dump(filmes, outfile)
    
else:
    print("Error:", response.status_code)
    print(response.text)
