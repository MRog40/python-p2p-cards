import random

"""
This class is just a list for holding cards
"""
class cards:
    cards = []
    # __init__    ->  Class instantiation, no arguments
    def __init__(self):
        self.cards = []

    # __str__     ->  The string representation of the cards object for printing
    def __str__(self):
        return ', '.join(self.cards)

    # add_deck    ->  One optional argument to specify adding more than one 52
    #                 card deck to the cards
    @classmethod
    def add_deck(self, decks = 1):
        # First I define two lists, one with the numbers and one with suits
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['S', 'H', 'C', 'D']
        # I then add a deck by extending the cards list by adding a list that is
        # every combination of the two previous lists
        for i in range(decks):
            self.cards.extend([''.join((r, s)) for r in ranks for s in suits])

    # add_joker   ->  One optional argument to specify adding more than one
    #                 joker to the deck
    @classmethod
    def add_joker(self, jokers = 1):
        # For the number of jokers specified, add a joker to the top of the pile
        for i in range(jokers):
            self.cards.append('J')
    
    # shuffle     ->  Randomly shuffle the cards
    @classmethod
    def shuffle(self):
        random.shuffle(self.cards)

    # sort        ->  Arrange the cards in order by suit, one argument that
    # specifies whether you like the values right to left 'rtl' default, or left
    # to right 'ltr', otherwise known as reverse order for pagans
    @classmethod
    def sort(self, direction='rtl'):
        self.cards.sort(key = lambda card: card[1])

    # deal        ->  remove cards from the top of the pile and add the removed
    #                 card to a new hand, then return a tuple of the amount of
    #                 hands that were specified. Deal the number of cards
    #                 specified by hand_size
    @classmethod
    def deal(self, hands, hand_size):
        # Create an empty tuple of size hands
        dealt_hands = tuple(cards() for i in range(hands))
        # For the number of cards to be dealt per hand
        for i in range(hand_size):
            # Put the top card from the deck into each hand
            for j in range(hands):
                dealt_hands[j].cards.append(self.cards.pop())
        return dealt_hands


deck = cards()

deck.add_deck()

deck.shuffle()

print(', '.join(deck.cards))
print(deck)
deck.sort()
print(deck)

