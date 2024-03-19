import requests
import json

# Function to send SPARQL queries to the DBpedia endpoint
def send_sparql_query(query):
    sparql_endpoint = "http://dbpedia.org/sparql"
    headers = {"Accept": "application/sparql-results+json"}
    params = {"query": query, "format": "json"}
    response = requests.get(sparql_endpoint, params=params, headers=headers)
    return response

# Function to process the results of SPARQL queries
def process_results(response, keys):
    if response.status_code == 200:
        # Extract JSON results from the response
        results = response.json()
        data = []
        # Iterate over the results to create a list of dictionaries
        for result in results["results"]["bindings"]:
            entry = {}
            # Fill the dictionary with values corresponding to the provided keys
            for key in keys:
                entry[key] = result.get(key, {}).get("value")
            data.append(entry)
        return data
    else:
        # In case of error, print the status code and response text
        print("Error:", response.status_code)
        print(response.text)
        return []

# Function to get movie information from DBpedia
def get_movies():
    query = """
    PREFIX dbo: <http://dbpedia.org/ontology/>
    SELECT DISTINCT ?movie ?title ?director ?writer ?musician ?duration WHERE {
        ?movie rdf:type dbo:Film ;
               rdfs:label ?title ;
               dbo:director ?director ;
               dbo:writer ?writer ;
               dbo:musicComposer ?musician ;
               dbo:runtime ?duration
        FILTER(lang(?title)='en') .
    } LIMIT 100
    """
    response = send_sparql_query(query)
    return process_results(response, ["movie", "title", "director", "writer", "musician", "duration"])

# Function to get actor information from DBpedia
def get_actors(movies):
    query = """
    PREFIX dbo: <http://dbpedia.org/ontology/>
    SELECT DISTINCT ?movie ?actor ?name ?abstract WHERE {
        ?movie dbo:starring ?actor .
        OPTIONAL { ?actor rdfs:label ?name . FILTER(lang(?name)='en') . }
        OPTIONAL { ?actor dbo:abstract ?abstract . FILTER(lang(?abstract)='en') . }
    }
    """
    response = send_sparql_query(query)
    return process_results(response, ["movie", "actor", "name", "abstract"])

# Function to add actor information to movie data
def add_actors_to_movies(movies, actors):
    for movie in movies:
        movie['elenco'] = [actor for actor in actors if actor['movie'] == movie['movie']]
    return movies

# Function to save data to a JSON file
def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Main program function
def main():
    # Get movie information from DBpedia
    movies = get_movies()
    # Get actor information from DBpedia
    actors = get_actors(movies)
    # Add actor information to movie data
    movies_with_actors = add_actors_to_movies(movies, actors)
    # Create a dictionary containing movie and actor data
    data = {'filmes': movies_with_actors, 'atores': actors}
    # Save data to a JSON file
    save_data(data, 'cinema.json')

# Check if the code is being run directly and call the main function
if __name__ == "__main__":
    main()
