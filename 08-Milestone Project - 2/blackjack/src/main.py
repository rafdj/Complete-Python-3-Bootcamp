colors_value = ["Carré", "Coeur", "Trèfle", "Pique"]

cards_value = {str(i): i for i in range(1, 10)}
cards_value.update({i: 10 for i in ['Valet', 'Dame', 'Roi']})
cards_value.update({'As': (1, 10)})
