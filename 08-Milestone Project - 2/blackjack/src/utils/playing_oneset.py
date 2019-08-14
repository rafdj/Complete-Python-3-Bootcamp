import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.card import *
from utils.player import *


def playing_oneset(players):
    """
    Playing one set of blackjack
    The game continue until :
        Crouper (players[0]) has 17 cards or
        No player ask for a card
    """
    player_index = 1
    while True:
        player = players[player_index]
        request_for_player = player.name + ", Do you want a card ? Y/N : "
        do_you_want_a_card = input(request_for_player)
        if do_you_want_a_card.strip().upper() == 'Y':
            player.game.append(Card.random_card())
            # Croupier add a card only if a player do it
            players[0].game.append(Card.random_card())
            player_index += 1
        elif do_you_want_a_card.strip().upper() == 'N':
            player_index += 1
        else:
            print("I did not understand your answer, please select Y(yes) or N(no)")
        if player_index == len(players):
            player_index = 1
        # TO DO : Add a test if all the players say no
        if max([len(player) == 17 for player in players]):
            break
