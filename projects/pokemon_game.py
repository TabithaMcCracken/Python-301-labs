# Done
# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


from unicodedata import name
import random
import csv
import time
from pathlib import Path
from csv import DictReader

hp_loss_decrement = 5   
hp_feed_increment = 5

class Pokemon():
    """models basic Pokemon"""

    def __init__(self, name, primary_type, max_hp, hp) -> None:
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def battle (self, computer_pokemon):
        print(
            f"You have chosen to battle with:\n"
            f"{user_pokemon.name} HP: {user_pokemon.hp}\n"
            f"The computer has chosen to battle with:\n"
            f"{computer_pokemon.name} HP: {computer_pokemon.hp}\n"
        )
        
        print("Let the battle begin...\n")
        time.sleep(3)

        result = self.determine_battle_result(computer_pokemon)

        print(
            f"Your Pokemon is a {self.primary_type} and theirs is a "
            f"{computer_pokemon.primary_type} type."
        )

        if result == "draw":
            print(f"It's a tie! You both loose {hp_loss_decrement} HP. \n")
            user_pokemon.change_hp(-hp_loss_decrement)
            computer_pokemon.change_hp(-hp_loss_decrement)
        elif result == "win":
            print(f"You win! The computer loses {hp_loss_decrement} HP.")
            computer_pokemon.change_hp(-hp_loss_decrement)
        else:
            print(f"You lose! You lose {hp_loss_decrement} HP.")
            self.change_hp(-hp_loss_decrement)

    def determine_battle_result(self, computer_pokemon):
                # water > fire > grass > water
        if self.primary_type == computer_pokemon.primary_type:
            return "draw"
        elif self.primary_type == "water" and computer_pokemon.primary_type == "fire":
            return "win"
        elif self.primary_type == "water" and computer_pokemon.primary_type == "grass":
            return "lose"
        elif self.primary_type == "fire" and computer_pokemon.primary_type == "grass":
            return "win"
        elif self.primary_type == "fire" and computer_pokemon.primary_type == "water":
            return "lose"
        elif self.primary_type == "grass" and computer_pokemon.primary_type == "water":
            return "win"
        else:
            return "lose"

    def change_hp(self, change):
        self.hp += change
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print(
                f"{self.name} has reached it's maximum HP of {self.hp}\n"
                f"It can't eat any more!"
            )
        elif self.hp <= 0:
            print(
                f"{self.name} has lost all it's HP and is now dead."
            )
        else:
            print(
                f"{self.name}'s current HP is now {self.hp}."
            )

    def __str__(self) -> str:
        return f"{self.name} {self.primary_type} {self.max_hp} {self.hp}"

    def __repr__(self) -> str:
        return "\n".join([self.name + ", Type: " + self.primary_type + ", HP: "
         + self.hp + ", Max HP: " + self.max_hp])

def get_computer_pokemon():
    computer_file_path = Path("/Users/tabithamccracken/Documents/codingnomads/"
        "python-301-main-copy/projects/computer_pokemon.csv")
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
    
    for pokemon in computer_list_of_pokemon:
        pokemon.hp = int(pokemon.hp)
        pokemon.max_hp = int(pokemon.max_hp)

    return computer_list_of_pokemon

def get_player_pokemon():
    player_file_path = Path("/Users/tabithamccracken/Documents/codingnomads/"
        "python-301-main-copy/projects/player_pokemon.csv")
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
    # convert hp and max_hp from str to int, can I do this above somewhere?
    for pokemon in player_list_of_pokemon:
        pokemon.hp = int(pokemon.hp)
        pokemon.max_hp = int(pokemon.max_hp)

    return player_list_of_pokemon
#Print stats of Pokemon
def print_pokemon_stats():
    print("Computer's Pokemon: \n")
    for pokemon in computer_list:
        print(
            f"{pokemon.name}, {pokemon.primary_type} type, HP"
            f" {pokemon.hp}, max HP {pokemon.max_hp}"
        )

    print("\nYour Pokemon: \n ")
    for pokemon in player_list:
        print(
            f"{pokemon.name}, {pokemon.primary_type} type, HP"
            f" {pokemon.hp}, max HP {pokemon.max_hp}"
        )

# User chooses a Pokemon to battle with
def get_user_choice():

    print_pokemon_stats()
    print(f"\nWhich Pokemon would you like to select?\n") 

    user_choice = input() 
    
    for pokemon in player_list:
        if user_choice == pokemon.name:
            return pokemon

# Computer chooses a Pokemon to battle with
def get_computer_choice():
        # Pick a random Pokemon from the list
        computer_choice = random.choice(computer_list)
        print(
            f"\nThe computer has chosen to battle with {computer_choice.name}. "
            f"They are a {computer_choice.primary_type} type. "
            f"Their HP is {computer_choice.hp} and their max HP "
            f"is {computer_choice.max_hp}.\n"
        )
        return computer_choice

def game_loop():
    while True:
        time.sleep(3)
        play_again = int(input(
            "\nWould you like to battle again[1], feed your Pokemon[2],"
            " view current scores[3] or exit the game[4]?"
        ))
        if play_again == 1:
            computer_pokemon = get_computer_choice()
            user_pokemon = get_user_choice()
            user_pokemon.battle(computer_pokemon)
        elif play_again == 2:
            user_pokemon = get_user_choice()
            user_pokemon.change_hp(5)
        elif play_again == 3:
            print_pokemon_stats()
        elif play_again == 4:
            break
        else:
            break

if __name__ == "__main__":
    #Setup
    # Get Pokemon from csv files
    print("Welcome to the Pokemon Game!\n")
    print(
        "In this game you nurture and battle your Pokemon against the "
        "computers Pokemon."
    )
    print("Good luck!")

    computer_list = get_computer_pokemon()
    player_list = get_player_pokemon()

    # Get user choice of Pokemon to battle with
    user_pokemon = get_user_choice()
    print(f"\nYou chose {user_pokemon.name} and your HP is {user_pokemon.hp}.")
    # Get computer pokemon
    computer_pokemon = get_computer_choice()

    # Play the game
    # Call Battle the battle between the user and the computer
    user_pokemon.battle(computer_pokemon)
    # Ask to play again, feed or end game
    game_loop()

    # Tear Down
    # Print results
    print("Good game! Here is the final HP's of all the Pokemon:")
    print_pokemon_stats()

