"""
Build a very basic Pokémon class that allows you to simulate battles
in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.

The class should follow these specifications:

- Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
- Primary types should be limited to `water`, `fire` and `grass`
- Implement a `battle()` method based on rock-paper-scissors that decides 
who wins based only on the `primary_type`:
       water > fire > grass > water
- Display messages that explain who won or lost a battle
- If a Pokemon loses a battle, they lose some of their `hp`
- If you call the `feed()` method on a Pokemon, they regain some `hp`
"""

import random
import time
from pathlib import Path
from csv import DictReader

computer_pokemon = "projects/Pokemon Game/computer_pokemon.csv"
player_pokemon = "projects/Pokemon Game/player_pokemon.csv"
hp_loss_decrement = 5   
hp_feed_increment = 5

class Pokemon():
    """Models basic Pokemon"""

    def __init__(self, name, primary_type, max_hp, hp) -> None:
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def battle (self, computer_pokemon):
        """Plays out the battle.

        Args:
            computer_pokemon (Pokemon): The computers Pokemon.
        """

        print(
            f"You have chosen to battle with:\n"
            f"{self.name} HP: {self.hp}\n"
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
            self.change_hp(-hp_loss_decrement)
            computer_pokemon.change_hp(-hp_loss_decrement)
        elif result == "win":
            print(f"You win! The computer loses {hp_loss_decrement} HP.")
            computer_pokemon.change_hp(-hp_loss_decrement)
        else:
            print(f"You lose! You lose {hp_loss_decrement} HP.")
            self.change_hp(-hp_loss_decrement)

    def determine_battle_result(self, computer_pokemon):
        """Returns whether the player wins, looses, or ties against the computer.

        Args:
            computer_pokemon (Pokemon): The computers Pokemon

        Returns:
            str: string with battle result
        """
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
        """Changes the Pokemons HP is the Pokemon is alive and their max HP
        hasn't been reached.

        Args:
            change (int): The amount of HP to change.
        """
        if self.hp > 0:
            self.hp += change

        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print(
                f"{self.name} has reached it's maximum HP of {self.hp}\n"
                f"It can't eat any more!"
            )
        elif self.hp <= 0:
            print(
                f"{self.name} has lost all it's HP and is dead."
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


def get_pokemon(file_path):
    """Returns the csv file of Pokemon as a list of Pokemon.

    Args:
        file_path (string): File path to the players list of Pokemon

    Returns:
        list: Pokemon list of players Pokemon
    """
    player_file_path = Path(file_path)
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
    # convert hp and max_hp from str to int
    for pokemon in player_list_of_pokemon:
        pokemon.hp = int(pokemon.hp)
        pokemon.max_hp = int(pokemon.max_hp)

    return player_list_of_pokemon

def print_pokemon_stats():
    """Prints the current status of all Pokemon."""

    print("\nComputer's Pokemon: \n")
    for pokemon in computer_list:
        print(
            f"{pokemon.name}, {pokemon.primary_type} type, HP"
            f" {pokemon.hp}, max HP {pokemon.max_hp}"
        )

    print("\nYour Pokemon: \n ")
    for pokemon in player_list:
        if pokemon.hp > 0:
            print(
                f"{pokemon.name}, {pokemon.primary_type} type, HP"
                f" {pokemon.hp}, max HP {pokemon.max_hp}"
            )
        else:
            print(
                f"{pokemon.name}, {pokemon.primary_type} type, HP"
                f" {pokemon.hp}, max HP {pokemon.max_hp} This Pokemon is dead."
            )

def get_user_choice():
    """Returns the users choice of Pokemon to use.

    Returns:
        Pokemon: The Pokemon the user has selected.
    """
    while True:
        print_pokemon_stats()
        print(f"\nWhich Pokemon would you like to select?\n") 

        user_choice = input()
        
        for pokemon in player_list:
            if user_choice == pokemon.name and pokemon.hp > 0:
                return pokemon
            elif user_choice == pokemon.name and pokemon.hp <= 0:
                print("That Pokemon is dead. Please select one that has an HP over 0.\n")


def get_computer_choice():
    """Returns the computers choice of Pokemon to use.

    Returns:
        Pokemon: computer's choice of a Pokemon
    """
    alive_pokemon = []

    for pokemon in computer_list:
        if pokemon.hp > 0:
            alive_pokemon.append(pokemon)

    computer_choice = random.choice(alive_pokemon)

    print(
        f"\nThe computer has chosen to battle with {computer_choice.name}. "
        f"They are a {computer_choice.primary_type} type. "
        f"Their HP is {computer_choice.hp} and their max HP "
        f"is {computer_choice.max_hp}.\n"
    )
    return computer_choice

def pokemon_alive(pokemon_list):
    """Determines if there are still Pokemon alive in a players list.

    Args:
        pokemon_list (Pokemon list): list of players Pokemon

    Returns:
        Boolean: returns whether there are Pokemon still alive
    """
    alive_pokemon = 0
    for pokemon in pokemon_list:
        if pokemon.hp > 0:
            alive_pokemon += 1
    if alive_pokemon > 0:
        return True
    else:
        return False

def game_loop():
    """Runs through the game after initial setup is complete.
    """
    while True:
        time.sleep(3)
        #Check to see if each player has Pokemon that are alive

        player_pokemon_alive = pokemon_alive(player_list)
        computer_pokemon_alive = pokemon_alive(computer_list)

        if player_pokemon_alive and computer_pokemon_alive: #both need to be true
            play_again = int(input(
                "\nWould you like to battle again[1], feed your Pokemon[2],"
                " view current scores[3] or exit the game[4]?"
            ))
            if play_again == 1:
                user_pokemon = get_user_choice()
                computer_pokemon = get_computer_choice()
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
        else:
            break
        
if __name__ == "__main__":
    """Initializes, runs, and ends the game.
    """

    print("Welcome to the Pokemon Game!\n")
    print(
        "In this game you nurture and battle your Pokemon against the "
        "computers Pokemon."
    )
    print("Good luck!")

    #Creates computer and players lists of Pokemon
    computer_list = get_pokemon(computer_pokemon)
    player_list = get_pokemon(player_pokemon)

    # Get users choice of Pokemon to battle with
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

