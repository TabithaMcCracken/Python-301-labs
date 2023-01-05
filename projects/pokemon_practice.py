from pathlib import Path
from csv import DictReader
from projects.pokemon_game import Pokemon

file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-301-main-copy/projects/pokemon.csv")
with open(file_path,"r") as file_in:
    dict_reader = DictReader(file_in)
    list_of_pokemon = list(dict_reader)

for pokemon in list_of_pokemon:
    print(pokemon["name"])
    Pokemon(pokemon["name"], pokemon["primary_type"], pokemon["max_hp"], pokemon["hp"])

