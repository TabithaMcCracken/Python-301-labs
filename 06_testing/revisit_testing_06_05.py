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

def get_page_content(url):
    """Gets the responsefrom a HTTP call to the URL"""
    page = requests.get(url)
    return page

def convert_to_json(response):
    pokemon_data = response.json()
    return pokemon_data

def create_list_of_pokemon_urls(pokemon_data):
    # pokemon_urls = [url['url'] for url in pokemon_data['results']]- not needed, can put in return statement
    return ([url['url'] for url in pokemon_data['results']])


def get_individual_pokemon_results_data(pokemon_url_list):
    list_of_pokemon_data = []
    for url in pokemon_url_list:
        poke_response = get_page_content(url)
        poke_result = convert_to_json(poke_response)
        list_of_pokemon_data.append(poke_result)

    return list_of_pokemon_data

def print_pokemon_data(pokemon_results):
        for poke_result in pokemon_results:
            print(f"Id type: {type(poke_result['id'])}")
            print(f"Id: {poke_result['id']}")   
            print(f"Name: {poke_result['name'].capitalize()}")
            print("Type/s:")
            for item in poke_result['types']:
                print(f"{item['type']['name']}")
            print("\n")


if __name__ == "__main__":
    response = get_page_content(BASE_URL)
    pokemon_data = convert_to_json(response)
    pokemon_url_list = create_list_of_pokemon_urls(pokemon_data)
    pokemon_results = get_individual_pokemon_results_data(pokemon_url_list)
    print_pokemon_data(pokemon_results)


    
