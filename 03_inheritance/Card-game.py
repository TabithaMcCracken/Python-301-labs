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
class Card:
    """ Standard playing cards"""
    def __init__(self, suit=0, rank=2) -> None: # default card is 2 of Clubs
        self.suit = suit
        self.rank = rank 

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                'Jack', 'Queen', 'King']
        
    def __less_than__ (self, other):
        if self.suit < other.suit: # Check suits first
            return True
        if self.suit>other.suit:
            return False

        return self.rank<other.rank #Check rank if suits are equal

    def __str__(self) -> str:
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

card1 = Card(2, 11)
print(card1)
    
