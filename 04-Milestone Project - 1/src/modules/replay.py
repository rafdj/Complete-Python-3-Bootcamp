def replay():
    """
        replay -> str
        Description: Allow to replay or not
        Outputs:
            "Y": the game restarts
            "N": the game stops
    """
    return input("Do you want to play again (Y/N) : ").upper().strip() == 'Y'
