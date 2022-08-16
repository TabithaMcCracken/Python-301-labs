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
            print(f"Both Pokemon are type {self.primary_type}, it's a tie! They both loose 5 HP. \n")
            user_pokemon.hp -= 5
            computer_pokemon.hp -= 5
            print(f"You HP is now: {user_pokemon.hp}\n")
        elif user_pokemon.primary_type == "water":
            if computer_pokemon.primary_type == "fire":
                print(f"Your Pokemon is a water type, theirs is a fire type, you win!")
                user_pokemon.hp += 5
                print(f"You HP is now: {user_pokemon.hp}")
            else:
                print("Your Pokemon is a water type and theirs is a grass, you loose!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")
        elif user_pokemon.primary_type == "fire":
            if computer_pokemon.primary_type == "grass":
                print("Your Pokemon is a fire type, theirs is a grass type, you win!")
                user_pokemon.hp += 5
                print(f"You HP is now: {user_pokemon.hp}")
            else:
                print("Your Pokemon is a fire type and theirs is a water type, you loose!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")
        elif user_pokemon.primary_type == "grass":
            if computer_pokemon.primary_type == "water":
                print("Your Pokemon is a grass type and theirs is a water type, you win!")
                user_pokemon.hp += 5
                print(f"You HP is now: {user_pokemon.hp}")
            else:
                print("Your Pokemon is a grass type and theirs is a fire type, you loose!")
                user_pokemon.hp -= 5
                print(f"Your HP is now {user_pokemon.hp}")

    def feed(self):
        self.hp += 5
        print(f"Your Pokemon now has an HP of: {self.hp}")

    def __str__(self) -> str:
        return f"{self.name} {self.primary_type} {self.max_hp} {self.hp}"



charmander = Pokemon("Charmander", "fire", 50, 50)
snivy = Pokemon("Snivy", "grass", 60, 60)
sobble = Pokemon("Sobble", "water", 60, 60)

possible_pokemon = [charmander, snivy, sobble]

# Take user input- which Pokemon do they want to battle with?

def get_user_choice():
    while True:
        user_choice = input("Which Pokemon would you like to battle with: Charmander, Snivy, or Sobble \n")
       
        if user_choice == charmander.name:
            return charmander
            # break
        elif user_choice == snivy.name:
            return snivy
            # break
        elif user_choice == sobble.name:
            return sobble
        else:
            print("Please try again.")

user_pokemon = get_user_choice()
print(f"You chose {user_pokemon.name} and your HP is {user_pokemon.hp}.")

# Computer chooses a Pokemon to battle which is not the same as the users


def get_computer_choice():
    while True:
        computer_choice = random.choice(possible_pokemon)
        # print(f"comp: {computer_choice.name}")
        if computer_choice.name != user_pokemon.name:
            print(f"The computer has chosen to battle with {computer_choice.name} and their HP is {computer_choice.hp}.")
            return computer_choice

computer_pokemon = get_computer_choice()


# Call Battle
user_pokemon.battle(computer_pokemon)


while True:
    play_again = int(input("Would you like to battle again[1], feed your Pokemon[2], or exit the game[3]?"))
    if play_again == 1:
        computer_pokemon = get_computer_choice()
        user_pokemon.battle(computer_pokemon)
    elif play_again == 2:
        user_pokemon.feed()
    elif play_again == 3:
        print(f"Good game! Your Pokemon ended with an HP of {user_pokemon.hp}.")
    else:
        break


# user_feed = input("Would you like to feed your Pokemon?\n")
# if user_feed == "Yes":
#     user_pokemon.feed()