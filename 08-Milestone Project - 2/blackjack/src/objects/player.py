"""
This module describes the object "Player" with its different function
It ccontains a relationship to the object "Card" which is one of the
caracteristics of a player
"""
from objects.card import *


# Import config
DEFAULT_BALANCE = 17000
DEFAULT_PLAYERNAME = "Croupier"
BLACKJACK_VALUE = 21


class Player():
    """
    Player is a class object with that describes only one player
    name : Name of the player, with a default value
    balance : The balance of cash of the player, with a default value
    game : list of cards of the players, empyt by default
    mise : the amount that should be played, 0 by default
    """
    def __init__(self, name=DEFAULT_PLAYERNAME, balance=DEFAULT_BALANCE, game=[], mise=0):
        """
        - if the name is empty or not provided, the player name should by the
        name by default
        - the balance value for the player by default is the balance value by
        default
        - if the balance value is not forced, it should take the balance value
        by default divided by the maximum number of rounds (17)
        - the initial game of a player, including the croupier, is empty
        """
        if name:
            self.name = name
        else:
            self.name = DEFAULT_PLAYERNAME
        self.balance = balance
        if self.name != DEFAULT_PLAYERNAME and self.balance == DEFAULT_BALANCE:
            self.balance = balance/17
        self.game = list(game)
        self.mise = mise

    def __len__(self):
        """
        len method return the number of cards in a player game
        """
        return len(self.game)

    def __str__(self):
        """
        print method retunr the name, the balance and all the game of a player
        """
        player_game_cards = ""
        i = 1
        for card in self.game:
            player_game_cards += "\nCard "+str(i)+" : ("+str(card.color)+", "+str(card.value)+", "+str(card.points)+")"
            i += 1
        return "Player name : "+self.name+"\nPlayer balance : "+str(self.balance)+"\nPlayer cards : "+player_game_cards

    def game_value(self):
        """
        Return the best combinaison of the player cards
        """
        try:
            game_value = sum(card.points for card in self.game)
        except:
            # Calculation should failed because of As in the game has 2 possible values
            game_value = 0
            for card in self.game:
                if card.value == "As":
                    # Maximize chances to be close to the blackjack value 21
                    if game_value+11 > BLACKJACK_VALUE:
                        game_value += 1
                    else:
                        game_value += 11
                        break
                else:
                    game_value += card.points
        return game_value
