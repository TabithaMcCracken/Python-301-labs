# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
import requests

response = requests.get(BASE_URL)
pokemon_data = response.json()

#print("Here is the info for 6 Pokemon:")
# print(pokemon_data['results'])
for item in pokemon_data['results']:
    poke_url = item['url']
    poke_response = requests.get(poke_url)
    poke_result = poke_response.json()
    print(f"Id: {poke_result['id']}")
    print(f"Name: {poke_result['name'].capitalize()}")
    print("Type/s:")
    for item in poke_result['types']:
        print(f"{item['type']['name']}")
    print("\n")


# poke_url = "https://pokeapi.co/api/v2/pokemon/7/"
# poke_response = requests.get(poke_url)
# poke_result = poke_response.json()

# print(f"Id: {poke_result['id']}")
# print(f"Name: {poke_result['name']}")
# for item in poke_result['types']:
#     print(f"Types: {item['type']['name']}")
