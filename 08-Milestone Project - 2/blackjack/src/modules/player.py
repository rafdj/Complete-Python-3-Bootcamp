import random

# Import config
balance_by_default = 17000
playername_by_default = "Croupier"


class Card():
    def __init__(self, color="", value="", points=0):
        self.color = color
        self.value = value
        self.points = points

    def __str__(self):
        return "Card color : "+self.color+"\nCard value : "+self.value+"\nNumber of points for this card : "+str(self.points)

    # This is Class attributes that define available parameters for a card
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


class Player():
    def __init__(self, name=playername_by_default, balance=balance_by_default, game=[]):
        if name:
            self.name = name
        else:
            self.name = playername_by_default
        self.balance = balance
        if self.name != playername_by_default and self.balance == balance_by_default:
            self.balance = balance/17
        self.game = game

    def __len__(self):
        return len(self.game)

    def __str__(self):
        return "Player name : "+self.name+"\nPlayer balance : "+str(self.balance)+"\nPlayer cards : "+str(self.game)
    
    def add_card_to_game(self):
        self.game.append(Card.random_card())
