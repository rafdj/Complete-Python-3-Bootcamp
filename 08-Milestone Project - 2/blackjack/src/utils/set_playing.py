import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.card import *
from utils.player import *


def set_init(players):
    """
    Put all players "mise" to 0
    Ask them their new mises
    Output : Update Player list
    """
    print("Faites vos jeux rien ne va plus !")
    players[0].game = []
    index = 1
    while index < len(players):
        player = players[index]
        # Reinitialize a player
        player.game = []
        player.mise = 0
        try:
            request_for_player = player.name+", how much do you wanna play ?" 
            mise = int(input(request_for_player))
            if mise > player.balance:
                print(player.name+" You don't have enough money, this is your sold :"+str(player.balance))
            elif mise == 0:
                print("Your amount must be bigger than 0")
            else:
                player.mise = mise
                index += 1
        except:
            print("I didn't understand your answer, please write an integer number")


def set_playing(players):
    """
    Playing one set of blackjack
    The set continue until :
        Crouper (players[0]) has 17 cards or
        No player ask for a card
    """
    player_index = 1
    croupier = players[0]

    while True:
        player = players[player_index]
        request_for_player = player.name + ", Do you want a card ? Y/N : "
        do_you_want_a_card = input(request_for_player)
        if do_you_want_a_card.strip().upper() == 'Y':
            new_card = Card.random_card()
            player.game.append(new_card)
            player_index += 1
            del(new_card)
        elif do_you_want_a_card.strip().upper() == 'N':
            player_index += 1
        else:
            print("I did not understand your answer, please select Y(yes) or N(no)")

        if player_index == len(players):
            if len(croupier) < 17:
                # All the players have been asked for a new card in the current round
                print("OK this round is up !")
                # Croupier add a card
                new_card = Card.random_card()
                croupier.game.append(new_card)
                del(new_card)
                player_index = 1
            else:
                # Reached maximum number of rounds
                break
