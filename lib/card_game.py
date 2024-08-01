from random import choice

from player import Player
from card import Card

class CardGame():
    def __init__(self) -> None:

        # create 52 instances of Card and store them in a list
        cards = []
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for value in range(1,14):
                cards.append(Card(suit, value))
        self.cards = cards

        self.shuffled = False

        # create instances of Player and choose a user.
        self.no_of_players = 4
        self.players = [Player() for i in range(self.no_of_players)]
        self.user = choice(self.players)

        # initialise an empty list so the trick can be stored
        self.trick = []
        self.trick_winner = None


    def shuffle_and_deal(self):
        """Share cards equally at random to players."""
        while len(self.cards) != 0:
            for i in range(self.no_of_players):
                card = choice(self.cards)
                self.cards.remove(card)
                self.players[i].hand.append(card)
        self.shuffled = True


    def _give_names(self):
        names = ["PLayer 1", "Player 2", "Player 3"]
        for player in self.players:
            if player == self.user:
                player.name = "User"
            else:
                player.name = choice(names)
                names.remove(player.name)

    def _get_number_of_cards_in_play(self):
        """Retrieve the number of cards left in the round."""
        number_of_cards = 0
        for player in self.players:
            number_of_cards += len(player.hand)
        print(f"{number_of_cards} cards remaining")
        return number_of_cards


    def find_first_trick_player(self):
        """Find the player with the 2 of clubs"""
        for player in self.players:
            for card in player.hand:
                if card.suit == "clubs" and card.value == 2:
                    return player


    def get_first_trick_order(self):
        """Put the player with the 2 of clubs at the start of the list"""
        # keeps the order of the players consistant just changes who goes first.
        # similar to playing the game going clockwise round the players.
        while self.players[0] != self.find_first_trick_player():
            player = self.players.pop()
            self.players.insert(0, player)

    def get_trick_order(self):
        """Put the winner of the previous trick at the start of the list"""
        while self.players[0] != self.trick_winner:
            player = self.players.pop()
            self.players.insert(0, player)


    def play_first_card_of_first(self):
        """Plays the 2 of clubs card automatically or allows user to input the card"""
        player = self.players[0]
        if player == self.user:
            print("You have the 2 of clubs.")
            while True: # infinite loop until player plays valid card.
                user_card = input("Play a card: ")
                if player._user_check_card_in_hand(user_card): 
                    card = player._get_card_from_user(user_card) 
                    if card.card == "2 of clubs":
                        player._play_card(card)
                        print(f"You played {user_card}.")
                        break
                print("Invalid card! Try again!")
        else:
            for card in player.hand: # plays 2 of clubs.
                if card.suit == "clubs" and card.value == 2:
                    player._play_card(card)
                    print(f"{player.name} has played {card.card}")
                    break
        self.trick.append(self.players[0].play) # appends 2 of clubs to trick list
        
    
    def _play_remaining_cards_of_trick(self):
        """Plays the rest of the trick using the first card as the leading suit"""
        for player in self.players[1:]: 
            if player == self.user:
                print("\nYour turn is next")
                print("Your hand:")
                player.show_hand()
                while True: # infinite loop until player plays valid card.
                    user_card = input("\nPlay a card: ")
                    if player._user_check_card_in_hand(user_card):
                        card = player._get_card_from_user(user_card)
                        # check the player has a card with the same suit as the leading suit.
                        if player._check_suit_in_hand(self.trick[0].suit): 
                            # ensure player plays a card match the leading suit if possbile
                            if card.suit == self.trick[0].suit:
                                player._play_card(card)
                                print(f"You have played the {card.card}\n")
                                break
                            else:
                                print(f"You must play a {self.trick[0].suit}")
                        # allows the player to play any card if hand doesn't contain leading suit
                        else:
                            player._play_card(card)
                            print(f"You have played the {card.card}")
                            break
                    else: 
                        print("Invalid Card! Try Again!")
            else:
                # check a bot has a card with the same suit as the leading suit.
                if player._check_suit_in_hand(self.trick[0].suit):
                    card = choice(player._get_cards_of_suit(self.trick[0].suit))
                    player._play_card(card)
                    print(f"{player.name} has played {card.card}")
                # plays a random card if bot's hand doesn't contain leading suit
                else:
                    card = choice(player.hand)
                    player._play_card(card)
                    print(f"{player.name} has played {card.card}")
            self.trick.append(player.play)

    def _get_trick_winner(self):

        trick_leading_suit = [card for card in self.trick if card.suit == self.trick[0].suit]
        highest_value_cards = sorted(trick_leading_suit, key=lambda card: card.value, reverse=True)
        self.trick_winner = self.players[self.trick.index(highest_value_cards[0])]

    def _give_winnings_to_player(self):
        self.trick_winner.won_cards.extend(self.trick)
    

    def _play_first_card_of_trick(self):
        """Plays the first card of the trick, doesn't allow bot or user to play hearts"""
        self.trick.clear()
        player = self.players[0] 
        if player == self.user:
            print("You won the last trick!")
            player.show_hand()
            while True: # infinite loop until player plays valid card
                user_card = input("Play a card: ")
                if player._user_check_card_in_hand(user_card):
                    card = player._get_card_from_user(user_card)
                    if card.suit != "hearts" or player._check_only_hearts():
                        player._play_card(card)
                        print(f"You have played the {card.card}")
                        break
                    else:
                        print("You can't lead with a hearts card")
                else:
                    print("Invalid Card! Try Again!")
        else:
            if player._check_only_hearts():
                card = choice(player.hand)
                player._play_card(card)
                print(f"{player.name} has played {card.card}")
            else:
                card = choice(player._get_non_hearts())
                player._play_card(card)
                print(f"{player.name} has played {card.card}")
        self.trick.append(player.play)

    def _show_user_winnings(self):
        for player in self.players:
            if player == self.user:
                player.show_winnings()
                break

    def _get_score(self):
        for player in self.players:
            for card in player.won_cards:
                if card.suit == "hearts":
                    player.score += 1
                if card.card == "12 of spades":
                    player.score += 13

    def _show_scores(self):
        for player in self.players:
            print(f"{player.name} scored {player.score} points.")

                
    def _play_trick(self):
        trick = 2
        while self._get_number_of_cards_in_play():
            print(f"\n---- Trick {trick} ----\n")
            trick += 1
            self.get_trick_order()
            self._play_first_card_of_trick()
            self._play_remaining_cards_of_trick()
            print(f"\nTrick: {[card.card for card in self.trick]}")
            # print([card.card for card in self.trick])
            self._get_trick_winner()
            print(f"\n{self.trick_winner.name } has won the trick")
            self._give_winnings_to_player()
            self._show_user_winnings()
            input("Press enter to play next trick:")


    def play_round(self):
        # first trick
        trick = 1
        self.shuffle_and_deal()
        self._give_names()
        self.get_first_trick_order()
        print(f"---- Trick {trick} ----")
        self.play_first_card_of_first()
        self._play_remaining_cards_of_trick()
        self._get_trick_winner()
        print(f"{self.trick_winner.name} has won the first trick")
        self._play_trick()
        self._get_score()
        self._show_scores()            




game = CardGame()
game.play_round()




        

        


    

    

        










