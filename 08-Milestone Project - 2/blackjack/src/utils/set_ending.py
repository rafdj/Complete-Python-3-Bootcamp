from utils.player import *
from utils.card import *


def set_ending(players):
    """
    Function to test if there is a winner in the game
    Inputs : List of Player
    Outputs : List of Player updated
    """
    croupier = players[0]
    if croupier.game_value() > 21:
        print("All the players have won")
        for player in players[1:]:
            player.balance += 1.5*player.mise
    elif croupier.game_value() == 21:
        print("All the players have lost")
        for player in players[1:]:
            player.balance = max(0, player.balance-player.mise)
    elif croupier.game_value() > 17:
        for player in players[1:]:
            if player.game_value() > croupier.game_value():
                print(player.name+" has won")
                player.balance += 1.5*player.mise
            elif player.game_value() > croupier.game_value():
                print(player.name+" has lost")
                player.balance -= player.mise

    return players
