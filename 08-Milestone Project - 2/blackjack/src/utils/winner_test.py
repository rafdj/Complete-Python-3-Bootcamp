from src.utils.player import *
from src.utils.card import *


def who_is_winner(players):
    """
    Function to test if there is a winner in the game
    Inputs : List of Player
    Outputs :
        the_winner : winner Player
        there_is_a_winnner : Boolean
    """
    croupier = players[0]
    if croupier.game_value() > 21:
        # All the players have won
        players = map(lambda player.balance: player.balance+1.5*player.mise, players)
    elif croupier.game_value() == 21:
        # All the players have lost
        players = map(lambda player.balance: max(0, player.balance-player.mise), players)
    elif croupier.game_value() > 17:
        for player in players[1:]:
            if player.game_value() > croupier.game_value():
                # Player with a bigger balance than croupier won
                player.balance += 1.5*player.mise
            elif player.game_value() == croupier.game_value():
                # Player with same balance get back their cash
                pass
            else:
                # Player with lower balance than croupier lost
                player.balance -= player.mise

    return players
