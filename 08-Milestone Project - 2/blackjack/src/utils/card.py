import random


class Card():
    def __init__(self, color="", value="", points=0):
        self.color = color
        self.value = value
        self.points = points

    def __str__(self):
        """
        print method of a card return the card value, its color and the number of points
        """
        return self.color+','+self.value+','+self.points

    # Class attributes to define available parameters for a card
    COLORS_VALUE = ["Carré", "Coeur", "Trèfle", "Pique"]

    CARDS_VALUE = {str(i): i for i in range(2, 10)}
    # Points values
    CARDS_VALUE.update({i: 10 for i in ['Valet', 'Dame', 'Roi']})
    CARDS_VALUE.update({'As': (1, 11)})

    @classmethod
    def random_card(cls):
        """
        Method to select a random card
        Output : Card object with random color, value and related number of
        points
        """
        selected_card_value = random.choice(list(cls.CARDS_VALUE.keys()))
        selected_card_points = cls.CARDS_VALUE[selected_card_value]
        cls.color = random.choice(cls.COLORS_VALUE)
        cls.value = selected_card_value
        cls.points = selected_card_points
        return cls
