import random


def choose_first():
    """
        choose_first -> str
        Description: Random select of the starting player
        Outputs:
            "Player 1" or "Player 2"
    """
    return "Player " + str(random.randint(1, 2))
