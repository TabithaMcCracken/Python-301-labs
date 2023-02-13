from pathlib import Path
from csv import DictReader
from pokemon_game import Pokemon

def get_computer_pokemon():
    computer_file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-301-main-copy/projects/computer_pokemon.csv")
    with open(computer_file_path,"r") as file_in:
        dict_reader = DictReader(file_in)
        computer_records = list(dict_reader)

    computer_list_of_pokemon = []
    for pokemon in computer_records:
        computer_list_of_pokemon.append(
            Pokemon(
                pokemon["name"], 
                pokemon["primary_type"], 
                pokemon["max_hp"], 
                pokemon["hp"]
            )
        )

    return computer_list_of_pokemon


def get_player_pokemon():
    player_file_path = Path("/Users/tabithamccracken/Documents/codingnomads/python-301-main-copy/projects/player_pokemon.csv")
    with open(player_file_path,"r") as file_in:
        dict_reader = DictReader(file_in)
        player_records = list(dict_reader)

    player_list_of_pokemon = []
    for pokemon in player_records:
        player_list_of_pokemon.append(
            Pokemon(
                pokemon["name"], 
                pokemon["primary_type"], 
                pokemon["max_hp"], 
                pokemon["hp"]
            )
        )

    for pokemon in player_list_of_pokemon:
        pokemon.hp = int(pokemon.hp)
        pokemon.max_hp = int(pokemon.max_hp)

    return player_list_of_pokemon

computer_list = get_computer_pokemon()
player_list = get_player_pokemon()

print("Here is the computer's list of Pokemon: \n")
for pokemon in computer_list:
    print(f"{pokemon.name}, {pokemon.primary_type} type, HP {pokemon.hp}, max HP {pokemon.max_hp}")
print("\n")

print("Here is your list of Pokemon: \n ")
for pokemon in player_list:
    print(f"{pokemon.name}, {pokemon.primary_type} type, HP {pokemon.hp}, max HP {pokemon.max_hp}")
