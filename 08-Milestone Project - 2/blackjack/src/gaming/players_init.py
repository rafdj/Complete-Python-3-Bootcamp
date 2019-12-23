import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from objects.card import *
from objects.player import *


def players_init():
    """
    Initialize the game with a requested number of players
    and a requested name for each player
    Output : List of Player
    """
    # Selection of players number
    while True:
        try:
            players_number = int(input("Please select a number of players : "))
        except:
            print("Please type a numeric number")
        else:
            if players_number == 0:
                print("Please select a number greater than 0")
            else:
                break

    # Players init starting by the croupier
    players = [Player()]
    i = 1
    while i <= players_number:
        introduction = "You are the number "+str(i)+"\nWhat is your name ? "
        while True:
            player_name = input(introduction)
            if player_name:
                break
            else:
                print("Please type a name")
        players.append(Player(name=player_name))
        i += 1
    return players
