# Done
# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.


import requests
import random
from pprint import pprint

# POKE API Search
limit = 100 # how many items to return from the api
offset = 100
BASE_URL = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}&offset={offset}"
response = requests.get(BASE_URL)
pokemon_data = response.json()

desired_poke = 'ghost'
desired_pokemon_list = []

for item in pokemon_data['results']:
    poke_url = item['url']
    poke_response = requests.get(poke_url)
    poke_result = poke_response.json()
    
    for item in poke_result['types']:
        if item['type']['name'] == desired_poke:
            desired_pokemon_list.append(poke_result['name'])

if len(desired_pokemon_list) == 0:
    raise SystemExit
else:
    print(f"Here are the {desired_poke} Pokemon:")
    for item in desired_pokemon_list:
        print(item.capitalize())

selected_pokemon = random.choice(desired_pokemon_list)


# GHIBLI API Search for Spirit 
GHIBLIAPI_BASE_URL = "https://ghibliapi-iansedano.vercel.app/api/species"


response = requests.get(GHIBLIAPI_BASE_URL)
film_data = response.json()
film_list = film_data['data']['species']

desired_ghibli = 'Spirit'
desired_ghibli_list = []

for item in film_list:
    if item['classification'] == desired_ghibli:
        desired_ghibli_list.append(item['name'])

print (f"Here are the {desired_ghibli} species from Ghibli: ")

if len(desired_ghibli_list) == 0:
    raise SystemExit
else:
    for item in desired_ghibli_list:
        print(item)
    
selected_ghibli = random.choice(desired_ghibli_list)

print(f"The randomly selected Ghibli is: {selected_ghibli} ")
print(f"The randomly selected Pokemon is: {selected_pokemon.capitalize()}")