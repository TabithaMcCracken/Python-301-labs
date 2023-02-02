import random
import os
import time


class Card:
    """ Standard playing cards"""
    def __init__(self, suit, rank, card_value):
        self.suit = suit
        self.rank = rank
        self.card_value = card_value

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    """Standard Deck"""
    def __init__(self) -> None:
        
        self.deck = []
        suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank_names = [
            "Ace", 
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King"
        ]
        card_values = {
            "Ace": 11, # Ace starts as an 11 & is changed to a 1 if hand goes over 21
            "2": 2, 
            "3": 3, 
            "4": 4, 
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10
        }

        for suit in suit_names:
            for card in rank_names:
                self._deck.append(Card(suit, card, card_values[card]))

    def shuffle(self):
        for i in range(len(self._deck) - 1, 0, -1):
            r = random.randint(0, i)
            self._deck[i], self._deck[r] = self._deck[r], self._deck[i]

    def deal_one(self):
        return self._deck.pop(-1)

    def __str__(self) -> str:
        return f"{self._deck}"

    def __repr__(self) -> str:
        return f"Deck: \n{self._deck}"
            
class Player:
    """Creates a player (which could be the dealer)"""
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0
    
    def give_card(self, card):
        self.cards.append(card)

    def wants_another_card(self):
        if self.score < 21:
            return True

class TwoPlayerGame:
    def __init__(self, deck, player_one, player_two):
        self.deck = deck
        self.deck.shuffle()
        self.player_one = player_one
        self.player_two = player_two
        self.player_score = 0
        self.dealer_score = 0

    def deal_two(self):
        for _ in range(2):
            self.player_one.give_card(self.deck.deal_one())

    def deal_one(self):
        self.player_one.give_card(self.deck.deal_one())
    
    def display_showing_cards(self):
        for card in self.player_two:
            player_score += player_two.card_value
            print(f"Player Score: {player_score}")

        

    def turn(self):
        if self.player_one.wants_another_card():
            self.player_two.give_card(self.deck.deal_one())

        if self.player_two.wants_another_card():
            self.player_two.give_card(self.deck.deal_one())

        self.print_showing_cards()
        self.evaluate_score()

    


    

class GameEngine:
    def __init__(self, dealer_score, player_score):
        self.game = TwoPlayerGame(Deck(), Player("Dealer"), Player("Tabitha"))
        self.game.deal()
        self.dealer_score = 0
        self.player_score = 0

    print(f"Player's Card:")
    print(f"{player_card.rank} of {player_card.suit}")
    # print(f"You're current score is: {player_score}")

    def evaluate_score():
        

    def another_card():


if __name__ == "__main__":
    GameEngine()


def game(deck):
    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    while len(player_cards) < 2:
        # Deal a card to the player
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value

        if len (player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        print(f"Player's Card:")
        print(f"{player_card.rank} of {player_card.suit}")
        print(f"You're current score is: {player_score}")

        print("Press Enter to continue")
        input()

        # Deal a card to the dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        print(f"Dealer's Card:")
        if len(dealer_cards) == 1:
            print(f"{dealer_card.rank} of {dealer_card.suit}")
            print(f"The dealer's current score is: {dealer_score}")
        else:
            print("The dealer's card is hidden.")
            print(f"The dealer's current showing score is: {(dealer_score)-dealer_cards[-1].card_value}")
        
        print("Press Enter to continue")
        input()

        if len (dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

    if player_score == 21:
        print("You have blackjack, you have won!")
        quit()

    while player_score < 21:

        player_choice = input("Enter H to hit or S to stay:\n")

        if player_choice.upper() == "H":
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
            player_score += player_card.card_value

            x = 0 # Check for Ace again
            while player_score > 21 and x < len(player_cards):
                if player_cards[x].card_value == 11:
                    player_cards[x].card_value = 1
                    player_score -= 10
                    x += 1
                else:
                    x += 1

            print(f"Player's Card:")
            print(f"{player_card.rank} of {player_card.suit}")
            print(f"You're current score is: {player_score}")

            print("Press Enter to continue")
            input()
        if player_choice.upper() == "S":
            break
        

    if player_score == 21:
        print("You have blackjack, you win!")
        quit()

    if player_score > 21:
        print("You busted! Game Over!")
        quit()

    while dealer_score < 17:
        print ("The dealer has decided to hit.")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        x = 0
        while dealer_score > 21 and x < len(dealer_cards):
            if dealer_cards[x].card_value == 11:
                dealer_cards[x].card_value = 1
                dealer_score -= 10
                x += 1
            else:
                x +=1

        print(f"Dealer's Card:")
        print(f"{dealer_card.rank} of {dealer_card.suit}")
        print(f"The dealer's current score is: {dealer_score}")

    if dealer_score > 21:
        print("The dealer busted, you win!")
    if dealer_score == 21:
        print("The dealer got a blackjack, you lose!")
    if dealer_score == player_score:
        print("Tie game!")
    elif player_score > dealer_score:
        print("You win!")

        




