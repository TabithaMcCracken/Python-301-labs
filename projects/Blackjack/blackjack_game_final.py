# Blackjack game
# The dealer acts as a player and is required to hit on 16, stay on 17

import random
import time

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
        suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_name = [
            'Ace',
            '2', 
            '3', 
            '4', 
            '5', 
            '6', 
            '7', 
            '8', 
            '9', 
            '10', 
            'Jack', 
            'Queen', 
            'King'
        ]
        card_value = {
            'Ace':11, 
            '2':2, 
            '3':3, 
            '4':4, 
            '5':5, 
            '6':6, 
            '7':7, 
            '8':8, 
            '9':9, 
            '10':10, 
            'Jack':10, 
            'Queen':10, 
            'King':10
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

    def print_cards(self):
        if self.isDealer == False:
            for card in self.cards:
                print(card)
        else:
            print("The first card is hidden.")
            for card in self.cards[1:]:
                print(card)

    def calculate_score(self):
        score = 0
        for card in self.cards:
            score += card.card_value
        self.score = score

        # Checks for 2 Aces in hand
        if len(self.cards) == 2:
            if self.cards[0].card_value == 11 and self.cards[1].card_value == 11:
                self.cards[0].card_value = 1
                self.score -= 10

        return self.score

    def get_card(self):
        dealt_card = random.choice(game_deck.deck)
        self.cards.append(dealt_card)
        game_deck.deck.remove(dealt_card)


if __name__ == '__main__':
    # Setup    
    # Create deck
    print("Welcome to Blackjack!")
    game_deck = Deck()
    game_deck.shuffle()
    print(repr(game_deck))
    # Create dealer and player
    dealer = Player("Dealer", True)
    player_name = input("What is your name?")
    player = Player(player_name, False)
    print(f"Welcome {player.name}!")
    print(f"You are playing the {dealer.name}.")

    print(f"Your current score is: {player.score}")
    print(f"The dealer's score is: {dealer.score}")

    # Deal 2 cards to player and dealer
    while len(dealer.cards) < 2:
        # Deal a card to the player
        player.get_card()

        # Print player cards and score      
        print("Your cards:")
        player.print_cards()
        player.calculate_score()
        print(f"\nYour score: {player.score}")

        time.sleep(3)

        # Deal a card to the dealer
        dealer.get_card()

        # Print dealer cards and score      
        print("Dealer cards:")
        dealer.print_cards()
        showing_score = dealer.calculate_score() - dealer.cards[0].card_value
        print(f"\nDealer's showing score: {showing_score}\n")

        time.sleep(3)
    
# Play game
# Evaluate if player or dealer has hit 21
# Ask player to stay or hit,  check for bust
# Determine if dealer stays or hits, check for bust
# Repeat until player no or bust
# Show scores and determine winner (if no one busted)
# Ask to play again 