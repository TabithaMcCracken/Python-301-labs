"""In this project, you'll create your own classes that allow you to model card games. 
Then, you'll use these classes to build a game.
Start by planning this project out using pencil and paper. 
Scribble ideas in your notebook and think about what classes you might need, 
which ones can inherit from another class, which operators do you want to implement, etc. 
Draw, write, scribble. Do whatever you need to do to get your brain going and 
draft a rough idea of what you'll need and how you'll approach this task.
Then start to write your custom classes.

Once you're done, try to build a card game that uses the classes you created. 
Share the game you built on your forum."""


""" Spades 3
    Hearts 2
    Diamonds 1
    Clubs 0

    Jack 11
    Queen 12
    King 13
"""

import random
import time

class Card:
    """ Standard playing cards"""
    def __init__(self, suit, rank, card_value):
        self.suit = suit
        self.rank = rank
        self.card_value = card_value

class Deck:
    def __init__ (self):
        self.deck = []

        suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                    'Jack', 'Queen', 'King']
        card_values = {'Ace':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                    '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10} 
        # Ace starts as an 11 and is changed to a 1 if hand goes over 21

        for suit in suit_names:
            for card in rank_names:
                self.deck.append(Card(suit, card, card_values[card]))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def __str__(self) -> str:
        return f"{self.deck}"

    def __repr__(self) -> str:
        return f"Deck: \n{self.deck}"



blackjack_deck = Deck()
blackjack_deck.shuffle()
print(blackjack_deck)


#class Deck():
#    def __init__(self) -> None:
#        self.cards = []
#        for suit in range(4):
#            for rank in range(1,14):
#                card = Card(suit, rank)
#                self.cards.append(card)