import random


class Card:
    """Standard playing cards"""

    def __init__(self, rank, suit):
        self.rank = ["A", "2" "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][rank-1]
        self.suit = "♠︎♣︎♥︎♦︎"[suit]
        self.card_value = rank

    def card_value(self):
        if self.card_value >= 10:
            return 10
        elif self.card_value == 1:
            return 11
        return card_value

    def show_card(self):
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print(f"|  {self.rank:<2}      |")
        print("|         |")
        print(f"|    {self.suit}    |")
        print("|         |")
        print(f"|      {self.rank:<2}  |")
        print("|⎽⎽⎽⎽⎽⎽⎽⎽⎽|")


    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self._deck = []

    def create_deck(self):
        for i in range(1,14):
            for j in range(4):
                self._deck.append(Card(i,j))

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
    def __init__(self, name, isDealer, deck):
        self.name = name
        self.isDealer = isDealer
        self.deck = deck
        self.cards = []
        self.score = 0

    def wants_another_card(self):
        if self.score < 21:
            return True

    def get_one_card(self, card):
        self.cards.append(card)


class TwoPlayerGame:
    def __init__(self, deck, player_one, player_two):
        self.deck = deck
        self.deck.shuffle()
        self.player_one = player_one
        self.player_two = player_two

    def deal(self):
        for _ in range(2):
            self.player_one.give_card(self.deck.deal_one())
            self.player_two.give_card(self.deck.deal_one())

    def take_turn(self):
        if self.player_one.wants_another_card():
            self.player_one.get_one_card(self.deck.deal_one())

        if self.player_two.wants_another():
            self.player_two.get_one_card(self.deck.deal_one())

    def display_cards(self):
        print(f"Dealer's Cards:\n")  
        for cards in self.player_one:
            if self.player_one[cards] == 0:
                print("The dealer's first card is hidden.")
            elif:
                cards.show_card()    
        print(f"Player's Cards:\n")
        for cards in self.player_two:
            cards.show_card()

class GameEngine:
    def __init__(self):
        self.game = TwoPlayerGame(Deck(), Player("Dealer"), Player("Tabitha"))
        self.game.deal()
        self.game.display_cards()

    def evaluate_score():
        # look at players hands, determine score
        ...
        


if __name__ == "__main__":
    GameEngine()