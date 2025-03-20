import requests
import json
import os

# Define API URL
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"

# Number of Pokémon to fetch
NUM_POKEMON = 50

# Ensure the directory exists
os.makedirs("model", exist_ok=True)

# File path
file_path = "model/data.json"

def fetch_pokemon_data(limit=NUM_POKEMON):
    """Fetch data for the first `limit` Pokémon from PokéAPI."""
    pokemon_data = []

    for i in range(1, limit + 1):
        response = requests.get(f"{POKEMON_API_URL}{i}/")
        if response.status_code == 200:
            data = response.json()
            pokemon_info = {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
            }
            pokemon_data.append(pokemon_info)
            print(f"Fetched {data['name']}")
        else:
            print(f"Failed to fetch Pokémon with ID {i}")

    return pokemon_data

def save_to_json(data, filepath):
    """Save data to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("Fetching Pokémon data...")
    data = fetch_pokemon_data()
    save_to_json(data, file_path)
    print(f"Data saved to {file_path}")
