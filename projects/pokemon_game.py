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

class Pokemon():
    """models basic Pokemon"""

    def __init__(self, name, primary_type, max_hp, hp) -> None:
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def battle (self, computer_pokemon):
        # water > fire > grass > water
        if self.primary_type == computer_pokemon.primary_type:
            print(f"Both Pokemon are type {self.primary_type}, it's a tie! You both loose 5 HP. \n")
            user_pokemon.hp -= 5
            computer_pokemon.hp -= 5
            print(f"You HP is now: {user_pokemon.hp}\n")
        elif user_pokemon.primary_type == "water":
            if computer_pokemon.primary_type == "fire":
                print(f"Your Pokemon is a water type, theirs is a fire type, you win!")
                computer_pokemon.hp -= 5
                print(f"Your HP is {user_pokemon.hp}")
            else:
                print("Your Pokemon is a water type and theirs is a grass, you loose 5 HP!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")
        elif user_pokemon.primary_type == "fire":
            if computer_pokemon.primary_type == "grass":
                print("Your Pokemon is a fire type, theirs is a grass type, you win!")
                computer_pokemon.hp -= 5
                print(f"Your HP is {user_pokemon.hp}")
            else:
                print("Your Pokemon is a fire type and theirs is a water type, you loose 5 HP!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")
        elif user_pokemon.primary_type == "grass":
            if computer_pokemon.primary_type == "water":
                print("Your Pokemon is a grass type and theirs is a water type, you win!")
                computer_pokemon.hp -= 5
                print(f"Your HP is {user_pokemon.hp}")
            else:
                print("Your Pokemon is a grass type and theirs is a fire type, you loose 5 HP!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")

    def feed(self):
        if self.hp <self.max_hp:
            self.hp += 1
            print(f"Your Pokemon now has an HP of: {self.hp}")
        else:
            print(f"Your Pokemon is at its maximum HP.")

    def __str__(self) -> str:
        return f"{self.name} {self.primary_type} {self.max_hp} {self.hp}"

charmander = Pokemon(
    name = "Charmander", 
    primary_type = "fire", 
    max_hp = 50, 
    hp = 50)

snivy = Pokemon(
    name = "Snivy", 
    primary_type = "grass",
    max_hp = 60, 
    hp = 60)

sobble = Pokemon(
    name = "Sobble", 
    primary_type = "water",
    max_hp = 60,
    hp = 60)

all_pokemon = [charmander, snivy, sobble]

# User chooses a Pokemon to battle with
def get_user_choice():
    while True:
        print(f"Which Pokemon would you like to battle with?") 
        for pokemon in all_pokemon:
            print(f"{pokemon.name}")
        user_choice = input() 

        for pokemon in all_pokemon:
            if user_choice == pokemon.name:
                return pokemon

# Get user choice of Pokemon to battle with
user_pokemon = get_user_choice()
print(f"You chose {user_pokemon.name} and your HP is {user_pokemon.hp}.")

# Makes a list of non-zero HP and non-user-selected Pokemon
def get_available_pokemon():
    usable_pokemon = []
    for pokemon in all_pokemon:
        if pokemon.hp > 0 and pokemon.name != user_pokemon.name:
            usable_pokemon.append(pokemon)
      
    print(f"Here are the other Pokemon that are alive:")
    for item in usable_pokemon:
        print(item.name)
    
    return usable_pokemon

# Computer chooses a Pokemon to battle which is not the same as the users
def get_computer_choice():
        # Pick a random Pokemon from the list
        possible_pokemon = get_available_pokemon()
        computer_choice = random.choice(possible_pokemon)
        print(f"The computer has chosen to battle with {computer_choice.name} and their HP is {computer_choice.hp}.")
        return computer_choice

# Get computer pokemon
computer_pokemon = get_computer_choice()

# Call Battle the battle between the user and the computer
user_pokemon.battle(computer_pokemon)


while True:
    if user_pokemon.hp > 0:
        play_again = int(input("Would you like to battle again[1], feed your Pokemon[2], or exit the game[3]?"))
        if play_again == 1:
            computer_pokemon = get_computer_choice()
            user_pokemon.battle(computer_pokemon)
        elif play_again == 2:
            user_pokemon.feed()
        elif play_again == 3:
            print(f"Good game! Your Pokemon ended with an HP of {user_pokemon.hp}.")
            break
        else:
            break
    else:
        print("Your Pokemon has no HP left and has died...")
        break

print("Here is the final HP's of all the Pokemon:")
for x in all_pokemon:
    print(f"{x.name}'s HP: {x.hp}")