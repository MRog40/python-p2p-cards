from cards import *

class Player:
    def __init__(self, name):
        self.hand = Cards()
        self.name = name

    def __str__(self):
        return "{:<12} {}".format(self.name + ': ', str(self.hand))

class MightyTable:
    def __init__(self):
        self.trick = Cards()
        self.discard = Cards()
        self.points = Cards()
        self.deck = Cards()
        
    def __str__(self):
        return "{:<12} {}".format('Table: ', str(self.deck))
