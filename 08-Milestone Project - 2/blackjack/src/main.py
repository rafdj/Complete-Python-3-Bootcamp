import sys
import os

sys.path.append(os.path.abspath(os.curdir)+"\\Complete-Python-3-Bootcamp\\08-Milestone Project - 2\\blackjack\\src")

from utils.card import *

colors_value = ["Carré", "Coeur", "Trèfle", "Pique"]

cards_value = {str(i): i for i in range(1, 10)}
cards_value.update({i: 10 for i in ['Valet', 'Dame', 'Roi']})
cards_value.update({'As': (1, 10)})

test_card = Card.random_card()
