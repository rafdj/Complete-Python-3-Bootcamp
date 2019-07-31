# Import config
balance_by_default = 17000
playername_by_default = "Croupier"
blackjack_value = 21


class Player():
    def __init__(self, name=playername_by_default, balance=balance_by_default, game=[]):
        """
        - if the name is empty or not provided, the player name should by the
        name by default
        - the balance value for the player by default is the balance value by
        default
        - if the balance value is not forced, it should take the balance value
        by default divided by the maximum number of rounds (17)
        - the initial game of a player, including the crouper, is empty
        """
        if name:
            self.name = name
        else:
            self.name = playername_by_default
        self.balance = balance
        if self.name != playername_by_default and self.balance == balance_by_default:
            self.balance = balance/17
        self.game = game

    def __len__(self):
        """
        len method return the number of cards in a player game
        """
        return len(self.game)

    def __str__(self):
        """
        print method retunr the name, the balance and all the game of a player
        """
        return "Player name : "+self.name+"\nPlayer balance : "+str(self.balance)+"\nPlayer cards : "+str(self.game)

    def game_value(self):
        """
        Return the best combinaison of the player cards
        """
        try:
            game_value = sum(card.points for card in player1.game)
        except:
            # Calculation should failed because of As in the game has 2 possible values
            game_value = 0
            for card in self.game:
                if card.value == "As":
                    # Maximize chances to be close to the blackjack value 21
                    if game_value+11 > blackjack_value:
                        game_value += 1
                    else:
                        game_value += 11
                        break
                else:
                    game_value += card.points
        return game_value
