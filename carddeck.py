import random

class cards:
    cards = []
    id = ''
    def __init__(self, id='deck'):
        self.cards = []
        self.id = id

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
    def order(self, direction='rtl'):
        return

    @classmethod
    def deal(self, hands, hand_size):
        dealt_hands = tuple(cards(str(i)) for i in range(hands))

        for i in range(hand_size):
            for j in range(hands):
                dealt_hands[j].cards.append(self.cards.pop())

        return dealt_hands

deck = cards

deck.add_deck()
deck.add_deck()

print(len(deck.cards))

print(deck.cards)
print()

deck.add_joker(1)

deck.shuffle()

print(deck.cards)
print()

len(deck.cards)
(h1, h2, h3, h4, h5) = deck.deal(5, 10)

print(h1.cards)
print(h2.cards)
print(h3.cards)
print(h4.cards)
print(h5.cards)
print(len(deck.cards))

