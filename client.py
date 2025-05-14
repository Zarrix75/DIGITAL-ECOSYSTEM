import requests

url = "https://zarrix75.github.io/DIGITAL-ECOSYSTEM/custom_data.json"

try:
    response = requests.get(url)
    response.raise_for_status()  # Vérifie si l'URL a bien été trouvée
    data = response.json()  # Récupère les données au format JSON
    print("Données récupérées avec succès :")
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la récupération des données : {e}")

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Gère les erreurs HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []

def display_movies(movies):
    for movie in movies:
        print(f"🎬 Title: {movie['name']}")
        print(f"   Description: {movie['description']}")
        print("   Specifications:")
        for key, value in movie["specifications"].items():
            print(f"     - {key.capitalize()}: {value}")
        print(f"   Tags: {', '.join(movie['tags'])}")
        print("-" * 40)

if __name__ == "__main__":
    url = "https://zarrix75.github.io/DIGITAL-ECOSYSTEM/custom_data.json"
    data = fetch_json_data(url)
    display_movies(data)
