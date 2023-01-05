from pathlib import Path
from csv import DictReader
from pokemon_game import Pokemon

file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-301-main-copy/projects/pokemon.csv")
with open(file_path,"r") as file_in:
    dict_reader = DictReader(file_in)
    records = list(dict_reader)

list_of_pokemon = []
for pokemon in records:
    print(pokemon["name"])
    list_of_pokemon.append(
        Pokemon(
            pokemon["name"], 
            pokemon["primary_type"], 
            pokemon["max_hp"], 
            pokemon["hp"]
        )
    )

