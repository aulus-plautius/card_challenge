from random import choice

from player import Player
from card import Card

class CardGame():
    def __init__(self) -> None:

        # create 52 instances of Card and store them in a list.
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
        self.dealer = choice(self.players)

        # initialise an empty list so the trick can be stored.
        self.trick = []
        self.trick_winner = None
        self.hearts_broken = False


    def give_names(self):
        """Randomly gives names to each player object."""
        names = ["Player 1", "Player 2", "Player 3"]
        for player in self.players:
            if player == self.user:
                player.name = "User"
            else:
                player.name = choice(names)
                names.remove(player.name)


    def generate_next_player(self):
        """Sets the next player attribute for each player object."""
        # sets next player as if players for standing in a circle. 
        # the next player will always be the same player for ech player.
        for i in range(self.no_of_players):
            self.players[i].next_player = self.players[(i+1) % self.no_of_players]
            self.players[i].opposite_player = self.players[(i+2) % self.no_of_players]
            self.players[i].previous_player = self.players[(i+3) % self.no_of_players]

    
    def print_table(self):
        if self.user:
            player_o = self.user.opposite_player.name
            player_l = self.user.previous_player.name
            player_r = self.user.next_player.name
            player_u = self.user.name
            print(f"              {player_o}")
            print("           +-----+-----+")
            print("           |           |")
            print(f"  {player_l} +           + {player_r}")
            print("           |           |")
            print("           +-----+-----+")
            print(f"               {player_u}")
        else:
            player = choice(self.players)
            player_o = player.opposite_player.name
            player_l = player.previous_player.name
            player_r = player.next_player.name
            player_u = player.name
            print(f"              {player_o}")
            print("           +-----+-----+")
            print("           |           |")
            print(f"  {player_l} +           + {player_r}")
            print("           |           |")
            print("           +-----+-----+")
            print(f"               {player_u}")




    def shuffle_and_deal(self):
        """Share cards equally at random to players."""
        player = choice(self.players)
        while len(self.cards) != 0:
                card = choice(self.cards)
                self.cards.remove(card)
                player.hand.append(card)
                player = player.next_player
        self.shuffled = True


    def _get_three_cards(self):
        player = self.dealer
        while True:
            player.passed_cards.clear() 
            if player == self.user:
                print("Your hand:\n")
                player.show_sorted_hand()
                while True: # infinite loop until valid card is picked
                    user_card = input("\nChoose a card: ")
                    if player.user_check_card_in_hand(user_card):
                        card = player.get_card_from_user(user_card)
                        player.passed_cards.append(card) 
                        player.hand.remove(card)
                        break
                    else:
                        print("Invalid Card! Try Again!")
                while True:
                    user_card = input("\nChoose a 2nd card: ")
                    if player.user_check_card_in_hand(user_card):
                        card = player.get_card_from_user(user_card)
                        player.passed_cards.append(card)
                        player.hand.remove(card)
                        break
                    else:
                        print("Invalid Card! Try Again!")
                while True:
                    user_card = input("\nChoose a 3rd card: ")
                    if player.user_check_card_in_hand(user_card):
                        card = player.get_card_from_user(user_card)
                        player.passed_cards.append(card)
                        player.hand.remove(card)
                        break
                    else:
                        print("Invalid Card! Try Again!")
            else:
                for i in range(3):
                    card = choice(player.hand)
                    player.passed_cards.append(card)
                    player.hand.remove(card)
            player = player.next_player
            if player == self.dealer:
                break



    def pass_cards_left(self):
        print("\n---- Pass Three Cards To The Left ----\n")
        self._get_three_cards()
        player = self.dealer
        while True: # passes cards to every player
            player.previous_player.hand.extend(player.passed_cards)
            player = player.next_player
            if player == self.dealer:
                break
        if self.user:
            user_passed_cards = [card.card for card in self.user.passed_cards]
            print(f"\nYou have passed the {", ".join(user_passed_cards)} to {self.user.previous_player.name}")
            user_recieved_cards = [card.card for card in self.user.next_player.passed_cards]
            print(f"\nYou have recieved the {", ".join(user_recieved_cards)} from {self.user.next_player.name}")

    def pass_cards_right(self):
        print("\n---- Pass Three Cards To The Right ----\n")
        self._get_three_cards()
        player = self.dealer
        while True:
            player.next_player.hand.extend(player.passed_cards)
            player = player.next_player
            if player ==self.dealer:
                break
        if self.user:
            user_passed_cards = [card.card for card in self.user.passed_cards]
            print(f"\nYou have passed the {", ".join(user_passed_cards)} to {self.user.next_player.name}")
            user_recieved_cards = [card.card for card in self.user.previous_player.passed_cards]
            print(f"\nYou have recieved the {", ".join(user_recieved_cards)} from {self.user.previous_player.name}")


    def pass_cards_opposite(self):
        print("\n---- Pass Three Cards Opposite ----\n")
        self._get_three_cards()
        player = self.dealer
        while True:
            player.opposite_player.hand.extend(player.passed_cards)
            player = player.next_player
            if player ==self.dealer:
                break 
        if self.user:
            user_passed_cards = [card.card for card in self.user.passed_cards]
            print(f"\nYou have passed the {", ".join(user_passed_cards)} to {self.user.opposite_player.name}")
            user_recieved_cards = [card.card for card in self.user.opposite_player.passed_cards]
            print(f"\nYou have recieved the {", ".join(user_recieved_cards)} from {self.user.opposite_player.name}")


    def get_number_of_cards_in_play(self):
        """Retrieve the number of cards left in the round."""
        number_of_cards = 0
        for player in self.players:
            number_of_cards += len(player.hand)
        return number_of_cards


    def find_first_trick_player(self):
        """Find the player with the 2 of clubs"""
        for player in self.players:
            for card in player.hand:
                if card.suit == "clubs" and card.value == 2:
                    self.trick_winner = player
                    break


    def play_first_card_of_first_trick(self):
        """Plays the 2 of clubs card automatically or allows user to input the card"""
        self.trick.clear()
        if self.trick_winner == self.user:
            print("You have the 2 of clubs.")
            while True: # infinite loop until player plays valid card.
                user_card = input("Play a card: ")
                print()
                if self.trick_winner.user_check_card_in_hand(user_card): 
                    card = self.trick_winner.get_card_from_user(user_card) 
                    if card.card == "2 of clubs":
                        self.trick_winner.play_card(card)
                        print(f"You played {user_card}.")
                        break
                print("Invalid card! Try again!")
        else:
            for card in self.trick_winner.hand: # plays 2 of clubs.
                if card.suit == "clubs" and card.value == 2:
                    self.trick_winner.play_card(card)
                    print(f"{self.trick_winner.name} has played {card.card}")
                    break
        self.trick.append(self.trick_winner.play) # appends 2 of clubs to trick list

    def play_remaining_cards_of_first_trick(self):
        player = self.trick_winner.next_player
        while player.next_player != self.trick_winner.next_player:
            if player == self.user:
                print("\nYour turn is next")
                print("Your hand:")
                player.show_sorted_hand()
                while True:
                    user_card = input("\nPlay a card: ")
                    if player.user_check_card_in_hand(user_card):
                        card = player.get_card_from_user(user_card)
                        # checks the input card is in the available cards
                        if card in player.get_first_trick_playable_cards():
                            player.play_card(card)
                            print(f"\nYou have played the {card.card}")
                            break
                    print("Invalid Card! Try Again!")
            else:
                availiable_cards = player.get_first_trick_playable_cards()
                card = choice(availiable_cards)
                player.play_card(card)
                print(f"{player.name} has played the {card.card}")
            self.trick.append(player.play)
            player = player.next_player

    def check_hearts_broken(self):
        if "hearts" in [card.suit for card in self.trick]:
            self.hearts_broken = True
        

    def play_first_card_of_trick(self):
        """Plays the first card of the trick, doesn't allow bot or user to play hearts""" 
        self.check_hearts_broken()
        self.trick.clear()
        if self.trick_winner == self.user:
            print("You won the last trick!")
            self.trick_winner.show_sorted_hand()
            while True: # infinite loop until player plays valid card
                user_card = input("\nPlay a card: ")
                if self.trick_winner.user_check_card_in_hand(user_card):
                    card = self.trick_winner.get_card_from_user(user_card)
                    # checks the input card is in the available cards
                    if card in self.trick_winner.get_first_card_of_trick(self.hearts_broken):
                        self.trick_winner.play_card(card)
                        print(f"\nYou have played the {card.card}")
                        break
                print("Invalid Card! Try Again!")
        else:
            availiable_cards = self.trick_winner.get_first_card_of_trick(self.hearts_broken)
            card = self.trick_winner.bot_first_card_choice(availiable_cards)
            self.trick_winner.play_card(card)
            print(f"{self.trick_winner.name} has played {card.card}")
        self.trick.append(self.trick_winner.play)



    def play_remaining_cards_of_trick(self):
        """Plays the rest of the trick using the first card as the leading suit"""
        player = self.trick_winner.next_player
        while player.next_player != self.trick_winner.next_player:
            if player == self.user:
                print("\nYour turn is next")
                print("Your hand:")
                player.show_sorted_hand()
                while True: # infinite loop until player plays valid card.
                    user_card = input("\nPlay a card: ")
                    if player.user_check_card_in_hand(user_card):
                        card = player.get_card_from_user(user_card)
                        if card in player.get_trick_playable_cards(self.trick): 
                            player.play_card(card)
                            print(f"\nYou have played the {card.card}")
                            break 
                    print("Invalid Card! Try Again!")
            else:
                availiable_cards = player.get_trick_playable_cards(self.trick)
                card = player.bot_choice(availiable_cards, self.trick)
                player.play_card(card)
                print(f"{player.name} has played {card.card}")
            self.trick.append(player.play)
            player = player.next_player


    def get_trick_winner(self):

        trick_leading_suit = [card for card in self.trick if card.suit == self.trick[0].suit]
        highest_value_cards = sorted(trick_leading_suit, key=lambda card: card.value, reverse=True)
        for player in self.players:
            if player.play == highest_value_cards[0]:
                self.trick_winner = player
                break


    def give_winnings_to_player(self):
        self.trick_winner.won_cards.extend(self.trick)


    def get_score(self):
        for player in self.players:
            for card in player.won_cards:
                if card.suit == "hearts":
                    player.score += 1
                if card.card == "12 of spades":
                    player.score += 13


    def get_maximum_score(self):
        return max([player.score for player in self.players])
        

    def show_scores(self):
        for player in self.players:
            print(f"{player.name} scored {player.score} points.")


    def reset_round(self):
        for player in self.players:
            self.cards.extend(player.won_cards)
            player.won_cards.clear()
            
        
            
    
