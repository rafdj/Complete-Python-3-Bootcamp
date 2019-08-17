import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.card import *
from utils.player import *


def set_playing(players):
    """
    Playing one set of blackjack
    The game continue until :
        Crouper (players[0]) has 17 cards or
        No player ask for a card
    """
    player_index = 1
    number_of_no = 0
    while True:
        player = players[player_index]
        request_for_player = player.name + ", Do you want a card ? Y/N : "
        do_you_want_a_card = input(request_for_player)
        if do_you_want_a_card.strip().upper() == 'Y':
            new_card = Card.random_card()
            player.game.append(new_card)
            # Croupier add a card only if a player do it
            players[0].game.append(new_card)
            player_index += 1
            del(new_card)
            number_of_no = 0
        elif do_you_want_a_card.strip().upper() == 'N':
            if number_of_no < 3:
                print("I did not understand your answer, please select Y(yes) or N(no)")
                player_index += 1
                number_of_no += 1
            else:
                print("OK this round is up ! Let's check who is the winner")
                break
        if player_index == len(players):
            # All the players have been asked for a new card in the current round 
            player_index = 1
        if max([len(player) == 17 for player in players]):
            # Reached maximum number of rounds
            break
    return players
