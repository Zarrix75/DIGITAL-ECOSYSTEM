import requests  # pour faire des requêtes HTTP (aller chercher le JSON en ligne)
 
# Fonction pour récupérer les données JSON depuis l'URL
def fetch_json_data(url):
    try:
        response = requests.get(url)  # envoie une requête GET à l'URL
        response.raise_for_status()  # pr gestion d'erreur
        return response.json()  # retourne le JSON sous forme de liste d'objets
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []
 
# Fonction pour afficher la liste des films
def display_movies(movies):
    for movie in movies:
        print(f"   Title: {movie['name']}")
        print(f"   Description: {movie['description']}")
        print("   Specifications:")
        for key, value in movie["specifications"].items():
            print(f"     - {key.capitalize()}: {value}")
        print(f"   Tags: {', '.join(movie['tags'])}")
        print("-" * 40)
 
# Programme principal
if __name__ == "__main__":
    url = "https://zarrix75.github.io/DIGITAL-ECOSYSTEM/custom_data.json"  # lien vers le JSON 
 
    data = fetch_json_data(url)  # récupère les données du fichier JSON
 
    print("Voici la liste des films disponibles :")
    display_movies(data)  # affiche tous les films