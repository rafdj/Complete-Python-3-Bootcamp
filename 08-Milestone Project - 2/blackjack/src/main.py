import sys
import os

os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.card import *
from utils.player import *
from utils.players_init import *
from utils.set_playing import *
from utils.set_ending import *

players = players_init()

while True:
    set_init(players)
    if max([player.mise for player in players[1:]]) == 0:
        print("Finished : No player want to play again")
        break
    else:
        set_playing(players)
        set_ending(players)
        if max([player.game_value() for player in players[1:]]) == 0:
            print("Finished : The bank has won ! All the players have lost")
            break
        elif max([player.game_value() == 21 for player in players[1:]]):
            print("Blackjack !! some players have won")
            winning_players = [player.name if player.game_value()==21 for player in players[1:]]
            print("Congratulations players")
            print(winning_players)
