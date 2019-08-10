import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.players_init import *

players = players_init()

there_is_a_winner = False
while not there_is_a_winner:
    # Croupier is the player 0 he never add cards to himself
    for player in players[1:]:
        while True: 
            request_for_player = player.name + ", Do you want a card ? Y/N : "
            do_you_want_a_card = input(request_for_player)
            if do_you_want_a_card.strip().upper() == 'Y':
                player.game.append(Card.random_card())
                # Croupier add a card only if a player do it
                player[0].game.append(Card.random_card())
                break
            elif do_you_want_a_card.strip().upper() == 'N':
                break
            else:
                print("I did not understand your answer, please select Y(yes) or N(no)")
    there_is_a_winner = True
    #TODO : Add the real test of winner 
