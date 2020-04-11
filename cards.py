import random

class cards:
    cards = []
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return repr(self.cards)

    def __str__(self):
        return ', '.join(self.cards)

    @classmethod
    def add_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['S', 'H', 'C', 'D']
        self.cards.extend([''.join((r, s)) for r in ranks for s in suits])

    @classmethod
    def add_joker(self, jokers = 1):
        for i in range(jokers):
            self.cards.append('J')
    
    @classmethod
    def shuffle(self):
        random.shuffle(self.cards)

    @classmethod
    def sort(self, direction='rtl'):
        self.cards.sort(key = lambda card: card[1])

    @classmethod
    def deal(self, hands, hand_size):
        dealt_hands = tuple(cards() for i in range(hands))
        for i in range(hand_size):
            for j in range(hands):
                dealt_hands[j].cards.append(self.cards.pop())
        return dealt_hands


"""
deck = cards()

deck.add_deck()

deck.shuffle()

print(', '.join(deck.cards))
print(deck)
deck.sort()
print(deck)
"""
