from src.utils.player import *
from src.utils.card import *


def there_is_a_winner(players):
    """
    Function to test if there is a winner in the game
    Inputs : List of Player
    Outputs :
        the_winner : winner Player
        there_is_a_winnner : Boolean
    """
    croupier = players[0]
    if croupier.game_value() > 21:
        players = map(lambda player.winner: True, players)
    elif croupier.game_value() == 21:
        players = map(lambda player.winner: False, players)
    elif croupier.game_value() > 17:
        for player in players[1:]:
            if player.game_value() > croupier:
                player.winner = True
                player.balance += 1.5*player.mise
            else:
                player.winner = False
    players[0].game_value == 21
    players[0].game_value > 17

    if players[0].game_value == 21:
        the_winner = players[0]
        there_is_a_winner = True
    elif 17 < players[0].game_value < 21:
        pass
    # TO DO : Define the real winning rule
    the_winner = players[0]
    there_is_a_winner = len(players[1])>4
    return the_winner, there_is_a_winner
