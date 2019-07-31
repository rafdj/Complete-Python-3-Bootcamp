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
        return (self.color, self.value, self.points)

    # Class attributes to define available parameters for a card
    colors_value = ["Carré", "Coeur", "Trèfle", "Pique"]

    cards_value = {str(i): i for i in range(2, 10)}
    # Points values
    cards_value.update({i: 10 for i in ['Valet', 'Dame', 'Roi']})
    cards_value.update({'As': (1, 10)})

    @classmethod
    def random_card(cls):
        """
        Method to select a random card
        Output : Card object with random color, value and related number of
        points
        """
        selected_card_value = random.choice(list(cls.cards_value.keys()))
        selected_card_points = cls.cards_value[selected_card_value]
        cls.color = random.choice(cls.colors_value)
        cls.value = selected_card_value
        cls.points = selected_card_points
        return cls
