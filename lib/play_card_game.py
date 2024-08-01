from cardgame import CardGame

game = CardGame()


trick = 1
game.give_names()
game.generate_next_player()
game.shuffle_and_deal()
print("\n-------- WELCOME TO HEARTS ---------\n")
game.print_table()
print(f"\nYou have been dealt 13 cards.\n")
game.pass_cards_left()
input("\nPress enter for the next pass")
game.pass_cards_right()
input("\nPress enter for the next pass")
game.pass_cards_opposite()
input("\nPress enter to start the round")
game.find_first_trick_player()
print(f"{game.trick_winner.name} has the 2 of clubs")
print(f"\n---- Trick {trick} ----\n")
print(f"{game.trick_winner.name} has the 2 of clubs, they go first!\n")
game.play_first_card_of_first_trick()
game.play_remaining_cards_of_trick()
game.get_trick_winner()
print(f"\n{game.trick_winner.name } has won the first trick")
game.give_winnings_to_player()
input("\n---- Press Enter To Play Next Trick ----")
trick = 2
while game.get_number_of_cards_in_play():
    print(f"\n---- Trick {trick} ----\n")
    trick += 1
    game.play_first_card_of_trick()
    game.play_remaining_cards_of_trick()
    game.get_trick_winner()
    print(f"\n{game.trick_winner.name } has won the trick")
    game.give_winnings_to_player()
    input("\n---- Press Enter To Play Next Trick ----")

print("---- Final Scores ----")
game.get_score()
game.show_scores()


        

        


    

    

        










