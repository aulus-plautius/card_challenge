from random import choice

class Player():
    def __init__(self) -> None:
        self.hand = []

    def show_hand(self):
        print([card.card for card in self.hand])


class Card():
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
        self.card = f"{value} of {suit}"


class CardGame():
    def __init__(self, no_of_players) -> None:

        cards = []
        suits = ["clubs", "diamonds", "hearts", "spaces"]
        for suit in suits:
            for value in range(1,14):
                cards.append(Card(suit, value))
        self.cards = cards

        # for i in range(no_of_players):
        #     self.players.append(Player())
        self.no_of_players = no_of_players
        self.players = [Player() for i in range(self.no_of_players)]

    def shuffle_and_deal(self):

        while len(self.cards) != 0:
            for i in range(self.no_of_players):
                card = choice(self.cards)
                self.cards.remove(card)
                self.players[i].hand.append(card)

        










