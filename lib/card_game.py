from random import choice

class Player():
    def __init__(self) -> None:
        self.hand = []
        self.play = None

    def show_hand(self):
        print([card.card for card in self.hand])

    def _user_play_card(self, card):
        hand_readable = [card.card for card in self.hand]
        if self._check_card_in_hand(card):
            self.play = self.hand[hand_readable.index(card)]
        else:
            return False

    def _check_card_in_hand(self, card):
        hand_card = [card.card for card in self.hand]
        if card in hand_card:
            return True
        else:
            return False

            

class Card():
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
        self.card = f"{value} of {suit}"


class CardGame():
    def __init__(self) -> None:

        cards = []
        suits = ["clubs", "diamonds", "hearts", "spaces"]
        for suit in suits:
            for value in range(1,14):
                cards.append(Card(suit, value))
        self.cards = cards
        self.shuffled = False

        self.no_of_players = 4
        self.players = [Player() for i in range(self.no_of_players)]

        self.round = []


    def shuffle_and_deal(self):
        while len(self.cards) != 0:
            for i in range(self.no_of_players):
                card = choice(self.cards)
                self.cards.remove(card)
                self.players[i].hand.append(card)
        self.shuffled = True

    def play_round(self):
        if self.shuffled:
            self.players[0].show_hand()
            while True:
                user_card = input("Choose a card to play: ")
                if self.players[0]._check_card_in_hand(user_card):
                    self.players[0]._user_play_card(user_card)
                    print(f"You played {user_card}.")
                    break
                else:
                    print("Invalid card! Try again!")
            self.round.append(self.players[0].play)
            for i in range(1,self.no_of_players):
                bot_card = choice(self.players[i].hand)
                self.players[i].play = bot_card
                self.round.append(self.players[i].play)
                print(f"A bot played {bot_card.card}")
        else: print("The deck must be shuffled!")


        

        


    

    

        










