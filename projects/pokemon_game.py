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

charmander = Pokemon(
    name = "Charmander", 
    primary_type = "fire", 
    max_hp = 50, 
    hp = 50
)

snivy = Pokemon(
    name = "Snivy", 
    primary_type = "grass",
    max_hp = 60, 
    hp = 60
)

sobble = Pokemon(
    name = "Sobble", 
    primary_type = "water",
    max_hp = 60,
    hp = 60
)

fennekin = Pokemon(
    name = "Fennekin",
    primary_type= "fire",
    max_hp = 70,
    hp = 70
)

wishiwashi = Pokemon(
    name = "Wishiwashi",
    primary_type = "water",
    max_hp = 30,
    hp = 30
)

caterpie = Pokemon(
    name = "Caterpie",
    primary_type = "grass",
    max_hp = 50,
    hp = 50
)

all_pokemon = [charmander, snivy, sobble, fennekin, wishiwashi, caterpie]

# User chooses a Pokemon to battle with
def get_user_choice():
    while True:
        print(f"Which Pokemon would you like to battle with?\n") 
        for pokemon in all_pokemon:
            print(
                f"{pokemon.name}, {pokemon.primary_type} type, HP:{pokemon.hp}"
            )
        user_choice = input() 

        for pokemon in all_pokemon:
            if user_choice == pokemon.name:
                return pokemon



# Makes a list of non-zero HP and non-user-selected Pokemon
def get_available_pokemon():
    usable_pokemon = []
    for pokemon in all_pokemon:
        if pokemon.hp > 0 and pokemon.name != user_pokemon.name:
            usable_pokemon.append(pokemon)
      
    print(f"Here are the other Pokemon that are alive:")
    for item in usable_pokemon:
        print(item.name)
    time.sleep(2)
    return usable_pokemon

# Computer chooses a Pokemon to battle which is not the same as the users
def get_computer_choice():
        # Pick a random Pokemon from the list
        possible_pokemon = get_available_pokemon()
        computer_choice = random.choice(possible_pokemon)
        print(
            f"\nThe computer has chosen to battle with {computer_choice.name}. "
            f"They are a {computer_choice.primary_type} type and "
            f"their HP is {computer_choice.hp}.\n"
        )
        return computer_choice


def game_loop():
    while True:
        time.sleep(3)
        if user_pokemon.hp > 0:
            play_again = int(input("Would you like to battle again[1], feed your Pokemon[2],"
                " or exit the game[3]?"
            ))
            if play_again == 1:
                computer_pokemon = get_computer_choice()
                user_pokemon.battle(computer_pokemon)
            elif play_again == 2:
                user_pokemon.change_hp(5)
            elif play_again == 3:
                print(
                    f"Good game! Your Pokemon ended with an HP of"
                    f" {user_pokemon.hp}."
                    )
                break
            else:
                break
        else:
            print("Your Pokemon has no HP left and has died...")
            break

if __name__ == "__main__":
    # Get user choice of Pokemon to battle with
    user_pokemon = get_user_choice()
    print(f"\nYou chose {user_pokemon.name} and your HP is {user_pokemon.hp}.")
    # Get computer pokemon
    computer_pokemon = get_computer_choice()

    # Call Battle the battle between the user and the computer
    user_pokemon.battle(computer_pokemon)
    game_loop()

    print("Here is the final HP's of all the Pokemon:")
    for x in all_pokemon:
        print(f"{x.name}'s HP: {x.hp}")