from cards import *

class player:
    def __init__(self, name):
        self.hand = cards()
        self.name = name

    def __str__(self):
        return self.name + ': ' + str(self.hand)

class mighty_tabl:
    def __init__(self, name):
        self.hand = cards()
        self.name = name

    def __str__(self):
        return self.name + ': ' + str(self.hand)

class mighty_table:
    def __init__(self, name):
        self.trick = cards()
        self.discard = cards()
        self.points = cards()
        self.deck = cards()
        self.name = name
        
    def __str__(self):
        return 'Table: ' + str(self.deck)
