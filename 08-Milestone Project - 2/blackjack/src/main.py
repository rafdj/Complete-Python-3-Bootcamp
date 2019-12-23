"""
This is the main file to run a blackjack party
"""


def main():
    """
    Main code function
    """
    import sys
    import os

    os.path.abspath(
        os.curdir) + "\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src"
    sys.path.append(
        os.path.abspath(
            os.curdir) +
        "\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

    from objects.card import *
    from objects.player import *
    from gaming.players_init import *
    from gaming.set_playing import *
    from gaming.set_ending import *

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
                winning_players = [
                    player.name for player in players[1:] if player.game_value() == 21]
                print("Congratulations players")
                print(winning_players)


if __name__ == "__main__":
    main()
