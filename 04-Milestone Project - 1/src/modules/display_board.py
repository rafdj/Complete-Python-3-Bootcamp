from IPython.display import clear_output


def display_board(board=['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
    """
        display_board -> NoneType
        Description: function to print the play board
        Inputs:
                board : list
        Outputs:
            Printed screen
    """
    clear_output()

    empty_line = 7*' '+'|'+7*' '+'|'+7*' '

    value_line = 3*' ' + '{}' + 3*' ' + '|' + 3*' '
    value_line += '{}' + 3*' ' + '|' + 3*' ' + '{}' + 3*' '

    underscore_line = 7*'_'+'|'+7*'_'+'|'+7*'_'

    print(empty_line)
    print(value_line.format(board[7], board[8], board[9]))
    print(underscore_line)
    print(empty_line)
    print(value_line.format(board[4], board[5], board[6]))
    print(underscore_line)
    print(empty_line)
    print(value_line.format(board[1], board[2], board[3]))
    print(empty_line)
