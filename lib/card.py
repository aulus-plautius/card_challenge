class Card():
    """A class to represent a card"""
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
        self.card = f"{value} of {suit}"