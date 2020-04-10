from cards import *

class player:
    def __init__(self, name):
        self.hand = cards(name)
        self.name = name

    def __str(self):
        return self.name + ': ' + str(self.cards)

class mighty_table:
    def __init__(self):
        self.trick = cards()
        self.discard = cards()
        self.points = cards()
        self.deck = cards()
        
