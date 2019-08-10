def there_is_a_winner(players_list):
    """
    Function to test if there is a winner in the game
    Inputs : List of Player
    Outputs :
        the_winner : winner Player
        there_is_a_winnner : Boolean
    """
    #TODO : Define the real winning rule
    the_winner = players_list[0]
    there_is_a_winner = len(players_list[1])>4
    return the_winner, there_is_a_winner
