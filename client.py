import requests

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []

def display_movies(movies):
    for movie in movies:
        print(f"   Title: {movie['name']}")
        print(f"   Description: {movie['description']}")
        print("   Specifications:")
        for key, value in movie["specifications"].items():
            print(f"     - {key.capitalize()}: {value}")
        print(f"   Tags: {', '.join(movie['tags'])}")
        print("-" * 40)

def find_movie_by_name(movies, movie_name):
    for movie in movies:
        if movie['name'].lower() == movie_name.lower():
            return movie
    return None

if __name__ == "__main__":
    url = "https://zarrix75.github.io/DIGITAL-ECOSYSTEM/custom_data.json"
    
    data = fetch_json_data(url)
    
    print("Voici la liste des films disponibles :")
    display_movies(data)
    
    favorite_movie = input("Quel est ton film préféré ? ")

    movie = find_movie_by_name(data, favorite_movie)
    
    if movie:
        print(f"\nVoici les informations sur ton film préféré : {favorite_movie}")
        print(f"   Title: {movie['name']}")
        print(f"   Description: {movie['description']}")
        print("   Specifications:")
        for key, value in movie["specifications"].items():
            print(f"     - {key.capitalize()}: {value}")
        print(f"   Tags: {', '.join(movie['tags'])}")
    else:
        print(f"Désolé, le film '{favorite_movie}' n'a pas été trouvé.")
