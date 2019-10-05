from src.utils.player import *
from src.utils.card import *


def set_ending(players):
    """
    Function to test if there is a winner in the game
    Inputs : List of Player
    Outputs : List of Player updated
    """
    croupier = players[0]
    if croupier.game_value() > 21:
        # All the players have won
        # players = map(lambda player.balance: player.balance+1.5*player.mise, players)
        for player in players:
            player.balance += 1.5*player.mise
        
    elif croupier.game_value() == 21:
        # All the players have lost
        # players = map(lambda player.balance: max(0, player.balance-player.mise), players)
        for player in players:
            player.balance = max(0, player.balance-player.mise)
    elif croupier.game_value() > 17:
        for player in players[1:]:
            if player.game_value() > croupier.game_value():
                # Player with a bigger balance than croupier won
                player.balance += 1.5*player.mise
            elif player.game_value() > croupier.game_value():
                # Player with lower balance than croupier lost
                player.balance -= player.mise

    return players
