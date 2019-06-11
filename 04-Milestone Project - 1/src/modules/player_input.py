def player_input():
    marker = ''
    while marker not in ('X', 'O'):
        marker = input("Please select your marker 'X' or 'O': ").upper()

    return marker
