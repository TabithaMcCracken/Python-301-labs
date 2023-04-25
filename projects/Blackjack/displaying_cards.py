import random
import os

class Card:
    def __init__(self, suit, rank, card_value):
        
        self.suit = suit # Suit of the Card like Spades and Clubs
        self.rank = rank # Representing Value of the Card like A for Ace
        self.card_value = card_value # Score Value for the Card like 10 for King

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.deck = []
        suit_name = [
            '\u2667', # Clubs
            '\u2662', # Diamonds
            '\u2661', #Hearts
            '\u2664' #Spades
        ]
        rank_name = [
            'A',
            '2', 
            '3', 
            '4', 
            '5', 
            '6', 
            '7', 
            '8', 
            '9', 
            '10', 
            'J', 
            'Q', 
            'K'
        ]
        card_value = {
            'A':11, 
            '2':2, 
            '3':3, 
            '4':4, 
            '5':5, 
            '6':6, 
            '7':7, 
            '8':8, 
            '9':9, 
            '10':10, 
            'J':10, 
            'Q':10, 
            'K':10
        } 
        # Ace starts as an 11 and is changed to a 1 if hand goes over 21

        for suit in suit_name:
            for rank in rank_name:
                self.deck.append(Card(suit, rank, card_value[rank]))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def __str__(self) -> str:
        return f"{self.deck}"

    def __repr__(self) -> str:
        return f"Deck: \n{self.deck}"
    

class Player:
    """Creates a player which could be the dealer
    """
    def __init__(self, name, isDealer) -> None:
        self.name = name
        self.isDealer = isDealer
        self.cards = []
        self.score = 0

    def calculate_score(self):
        score = 0
        for card in self.cards:
            score += card.card_value
        self.score = score

        # Checks for 2 Aces in hand, change 1st one to value 1
        if len(self.cards) == 2:
            if self.cards[0].card_value == 11 and self.cards[1].card_value == 11:
                self.cards[0].card_value = 1
                self.score -= 10

        # Checks to see if Ace should be an 11 or changed to a 1 if the hand is over 21
        x = 0
        while self.score > 21 and x < len(self.cards):
            if self.cards[x].card_value == 11:
                self.cards[x].card_value = 1
                self.score -= 10
                x += 1
            else:
                x += 1

        return self.score

    def get_card(self):
        dealt_card = random.choice(game_deck.deck)
        self.cards.append(dealt_card)
        game_deck.deck.remove(dealt_card)


game_deck = Deck()
game_deck.shuffle()

dealer = Player("Dealer", True)
player = Player("Player", False)

print("We will now deal 2 cards to each player.")

# Deal 2 cards to player and dealer
while len(dealer.cards) < 2:
    # Deal a card to the player, print cards and score
    player.get_card()

    # Deal a card to the dealer, print cards and score
    dealer.get_card() 


CARD_SLICES = [
    " _________________",
    "|                 |",
    "|   {rank}            |",  # 2
    "|                 |",
    "|                 |",
    "|                 |",
    "|        {suit}        |",
    "|                 |",
    "|                 |",
    "|                 |",
    "|            {rank}   |",  # 9
    "|_________________|",
]

HIDDEN_CARD_SLICES = [
    " ________________",
    "| !              |",
    "|      * *       |",
    "|    *     *     |",
    "|          *     |",
    "|         *      |",
    "|       *        |",
    "|       *        |",
    "|                |",
    "|                |",
    "|       *     !  |",
    "|________________|",
]

def print_cards_fancy(player):
    print(f"\n=={player.name}'s Cards==")
    for card_slice, hidden_slice in zip(CARD_SLICES, HIDDEN_CARD_SLICES):
        if player.isDealer:
            card_slices = "\t".join(
                [   
                        card_slice.format(rank = card.rank + (" " if len(card.rank) == 1 else ""), 
                        suit = card.suit + "") for card in player.cards[1:]

                ]
            )
            print(f"{hidden_slice}\t{card_slices}")
        else:
            card_slices = "\t".join(
                [   
                        card_slice.format(rank = card.rank + (" " if len(card.rank) == 1 else ""), 
                        suit = card.suit + "") for card in player.cards

                ]
            )
            print(f"{card_slices}\t{hidden_slice if player.isDealer else ''}") # Still not sure what the second tab section is for

print_cards_fancy(dealer)
print(dealer.cards)
input("Press Enter to Continue")

def clear():
    os.system("clear")

clear()
print_cards_fancy(player)
print(player.cards)


# Replaces line 14
# print(f"\t{card_slices}\t{hidden_slice if hidden else ''}")