class Player():
    """A class to represent a player"""
    def __init__(self) -> None:
        self.hand = []
        self.play = None
        self.name = None
        self.won_cards = []
        self.score = 0

    def show_hand(self):
        hand = [card.card + "," for card in self.hand]
        for i in range(0, len(hand), 5):
            row = hand[i:i + 5]
            print(" ".join(row))

    def show_winnings(self):
        winnings = [card.card + "," for card in self.won_cards]
        for i in range(0, len(winnings), 4):
            row = winnings[i:i + 4]
            print(" ".join(row))
        
        
    def _play_card(self, card):
        self.play = card
        self.hand.remove(card)

    def _check_card_in_hand(self, card):
        return card in self.hand
    
    def _user_check_card_in_hand(self, user_card):
        user_hand = [card.card for card in self.hand]
        if user_card in user_hand:
            return True
        else:
            return False


    def _check_suit_in_hand(self, suit):
        return suit in [card.suit for card in self.hand]
            
    def _get_cards_of_suit(self, suit):
        return [card for card in self.hand if card.suit == suit]

        
    
    def _get_card_from_user(self, user_card):
        for card in self.hand:
            if card.card == user_card:
                return card
            
    def _check_only_hearts(self):
        for card in self.hand:
            if card.suit != "hearts":
                return False
        return True