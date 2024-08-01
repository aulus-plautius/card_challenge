class Player():
    """A class to represent a player"""
    def __init__(self) -> None:
        self.hand = []
        self.play = None
        self.name = None
        self.won_cards = []
        self.score = 0
        self.next_player = None
        self.previous_player = None
        self.opposite_player = None
        self.passed_cards = []


    def show_sorted_hand(self):
        for suit in ["clubs", "diamonds", "spades", "hearts"]:
            cards_of_suit = [card for card in self.hand if card.suit == suit]
            sorted_suit = sorted(cards_of_suit, key=lambda card: card.value)
            sorted_suit_cards = [card.card for card in sorted_suit]
            if sorted_suit_cards:
                print(f"{suit.title()}:  \t" + ", ".join(sorted_suit_cards) + ";")


    def show_hand(self):
        hand = [card.card + "," for card in self.hand]
        for i in range(0, len(hand), 4):
            row = hand[i:i + 4]
            print(" ".join(row))


    def show_winnings(self):
        for suit in ["clubs", "diamonds", "spades", "hearts"]:
            cards_of_suit = [card for card in self.won_cards if card.suit == suit]
            sorted_suit = sorted(cards_of_suit, key=lambda card: card.value)
            sorted_suit_cards = [card.card for card in sorted_suit]
            if sorted_suit_cards:
                print(f"{suit.title()}:  \t" + ", ".join(sorted_suit_cards) + ";")


    def play_card(self, card):
        self.play = card
        self.hand.remove(card)


    def _check_card_in_hand(self, card):
        return card in self.hand


    def user_check_card_in_hand(self, user_card):
        user_hand = [card.card for card in self.hand]
        if user_card in user_hand:
            return True
        else:
            return False


    def check_suit_in_hand(self, suit):
        return suit in [card.suit for card in self.hand]
    

    def get_cards_of_suit(self, suit):
        if "12 of spades" in [card.card for card in self.hand]:
            return [card for card in self.hand if card.suit == suit or card.card == "12 of spades"]
        else:
            return [card for card in self.hand if card.suit == suit]

        
    def get_card_from_user(self, user_card):
        for card in self.hand:
            if card.card == user_card:
                return card
            

    def check_only_hearts(self):
        for card in self.hand:
            if card.suit != "hearts":
                return False
        return True


    def get_non_hearts(self):
        return [card for card in self.hand if card.suit != "hearts"]