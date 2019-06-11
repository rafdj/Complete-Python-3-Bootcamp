def player_choice(board):
    while True:
        position = input("Please select your position : ")
        if position.isnumeric():
            position = int(position)
            if position > 9:
                print("Please select a number between 1 and 9")
            elif space_check(board, position):

                return(position)
                break
