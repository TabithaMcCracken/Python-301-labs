"""
Build a text-based role-playing game that has at least two classes:

Hero(): the protagonist of your game that the player controls and identifies with. 
There should be only one hero.
Opponent(): the challengers that the player meets throughout the gameplay. There should be multiple opponents.

The hero should encounter multiple opponents of different strengths or levels. 
They should be able to perform different actions when meeting an opponent. 
These actions should be at a minimum:

attack
or run away

If the Hero chooses to attack, the program decides through a simulated dice throw 
that takes the current level into account, whether the hero or the opponent wins this round:
Also implement consequences for winning and losing, e.g. forcing the hero to wait 
a few seconds before continuing the game in case they lose. Or removing the opponent 
from the opponent pool in case the hero wins.
You'll have to implement both attributes and methods for both of your classes. 
Think about what you'll need so you can model the described functionality. Map out the project before you start coding.

Hints
There is a small Python RPG Game available on GitHub, that implements the described tasks. 
It allows you to safely defuse your digital rage against Paywalls, PHP, and even Wordpress sites! 
You can look at the code to get some inspiration.

However, I strongly suggest that you think about it deeply first and that you build your own idea. 
Translating ideas into code by yourself is an incredibly useful technique to facilitate your learning, and working on something that you are interested in makes coding more fun.

How to play the pre-made game
To interact with the example game solution, download the repo and run the file main.py in a Python 3 environment. You then have a few possible actions that you can access with keyboard inputs:

type l to look around
type a to attack
type r to run away
Can you defeat all the scary opponents lurking in this game?
"""

from unicodedata import name
import random

class Hero():
    """This is our hero"""

    def __init__(self, name, strength) -> None:
        self.name = name
        self.strength = strength

    def attack(self, random_opponent):
        print(f"{self.name} will battle {random_opponent.name}")
    
class Opponent():
    """This is our opponent"""

    def __init__(self, name, strength) -> None:
        self.name = name
        self.strength = strength


hero_name = str(input("What is the name of your hero?"))
hero = Hero(hero_name, 10)

opponents= [
    Opponent("Godzilla", 10),
    Opponent("Ursula", 9)
    ]

current_opponent = random.choice(opponents)
print(f"Your current opponent is: {current_opponent.name}")

user_action = input("Would you like to attack[a] or run away[r]?")
if user_action == "a":
    hero.attack(current_opponent)
elif user_action == "r":
    print("You have decided to run away.")
else:
    print("Invalid input")