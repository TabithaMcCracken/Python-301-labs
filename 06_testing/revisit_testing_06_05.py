# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.


# 04_03_poke_info.py
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
import requests
import json

number_pokemon_requested = 8
BASE_URL = f"https://pokeapi.co/api/v2/pokemon/?limit={number_pokemon_requested}&offset=0"

def get_page_content(url): # Test complete
    """Gets the responsefrom a HTTP call to the URL"""
    return requests.get(url)

def convert_to_json(url): # Test complete
    response = get_page_content(url)
    return response.json()

def create_list_of_pokemon_urls(url): # Test complete
    pokemon_data = convert_to_json(url)
    # pokemon_urls = [url['url'] for url in pokemon_data['results']]- not needed, can put in return statement
    return ([url['url'] for url in pokemon_data['results']])

def get_individual_pokemon_results_data(url): # Test complete
    pokemon_url_list = create_list_of_pokemon_urls(url)
    list_of_pokemon_data = []
    for url in pokemon_url_list:
        poke_result = convert_to_json(url)
        list_of_pokemon_data.append(poke_result)
    return list_of_pokemon_data

def get_poke_id(poke_result):
    return poke_result['id']

def get_poke_name(poke_result):
    return poke_result['name']

def get_poke_types(poke_result):
    types_list = [item['type']['name'] for item in poke_result['types']]
    return types_list
        

if __name__ == "__main__":

    pokemon_results = get_individual_pokemon_results_data(BASE_URL)

    for item in pokemon_results:
        id = get_poke_id(item)
        print(f"Id: {id}")

        name = get_poke_name(item)
        print(f"Name: {name.capitalize()}")

        poke_types = get_poke_types(item)
        print("Type/s:")
        for item in poke_types:
            print(f"{item}")
        print("\n")



    
