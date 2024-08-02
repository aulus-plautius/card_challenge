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
        """Print the user's current hand in a sorted readable format"""
        for suit in ["clubs", "diamonds", "spades", "hearts"]:
            cards_of_suit = [card for card in self.hand if card.suit == suit]
            sorted_suit = sorted(cards_of_suit, key=lambda card: card.value)
            sorted_suit_cards = [card.card for card in sorted_suit]
            if sorted_suit_cards:
                print(f"{suit.title()}:  \t" + ", ".join(sorted_suit_cards) + ";")


    def show_hand(self):
        """Print the user's current hand"""
        hand = [card.card + "," for card in self.hand]
        for i in range(0, len(hand), 4):
            row = hand[i:i + 4]
            print(" ".join(row))


    def show_winnings(self):
        """Show the users won cards in a sorted readable format"""
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


    def get_card_from_user(self, user_card):
        """Retrieve card object from user in put"""
        for card in self.hand:
            if card.card == user_card:
                return card

    
    def get_first_trick_playable_cards(self):
        """Return the availiable cards a player can play in the first trick"""
        suits = [card.suit for card in self.hand]
        if "clubs" in suits:
            return [card for card in self.hand if card.suit == "clubs"]
        else:
            return [card for card in self.hand if card.suit != "hearts" and card.card != "12 of spades"]
    
    def get_first_card_of_trick(self, hearts_broken):
        """Return the availiable cards a player can play on first card of a trick"""
        if hearts_broken:
            return self.hand
        # if hearts have not been broken, they cannot be lead with
        else:
            return [card for card in self.hand if card.suit != "hearts"]
        

    def get_trick_playable_cards(self, trick):
        """Retrieve the availiable cards a player can play during a trick"""
        leading_suit = trick[0].suit
        suits = [card.suit for card in self.hand]
        availiable_cards = []
        if leading_suit in suits:
            for card in self.hand:
                # if the leading suit in players hand it can only play that suit
                # or the 12 of spades
                if card.suit == leading_suit:
                    availiable_cards.append(card)
                elif card.card == "12 of spades":
                    availiable_cards.append(card)
            return availiable_cards
        # if the leading suit is not in the bots hand, it can play from any card
        else: 
            return self.hand
        

    def bot_choice(self, availiable_cards, trick):
        """Intelligent card pick for a bot."""
        suits = [card.suit for card in availiable_cards]
        cards = [card.card for card in availiable_cards]
        # if the leading suit is not a spade and the bot is able to play any card
        # and has the 12 of spades, it will play it as it wouldn't win it back.
        if "12 of spades" in cards and trick[0].suit != "spades":
            return next(card for card in availiable_cards if card.card == "12 of spades")
        elif "hearts" in suits:
            hearts = [card for card in availiable_cards if card.suit == "hearts"]
            sorted_hearts = sorted(hearts, key=lambda card: card.value)
            # if the leading suit isn't a heart the bot will play a high value heart
            if trick[0].suit != "hearts":
                return sorted_hearts[-1]
            # if the leading suit is a heart the bot will play a low value heart
            else:
                return sorted_hearts[0]
        # the bot will play a lowest value card in it's avaialible hand.
        else:
            sorted_cards = sorted(availiable_cards, key=lambda card: card.value)
            return sorted_cards[0]
        
    def bot_first_card_choice(self, availiable_cards):
        """Intelligent first card pick for a bot"""
        # sorts hand so 12 of spades and high value hearts are at the end, and
        # then the bot picks the first card in it's hand
        sorted_cards = []
        suits = []
        for suit in ["clubs", "diamonds", "spades"]:
            suits.extend([card for card in availiable_cards if card.suit == suit])
        sorted_cards.extend(sorted(suits, key=lambda card: card.value))
        hearts = [card for card in availiable_cards if card.suit == "hearts"]
        sorted_hearts = sorted(hearts, key=lambda card: card.value)
        sorted_cards.extend(sorted_hearts)
        return sorted_cards[0]
    


                