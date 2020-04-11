import random

"""
This class is just a list for holding cards
"""
class Cards:
    # __init__    ->  Class instantiation, no arguments
    def __init__(self, decks = 0):
        self.cards = []

    # __str__     ->  The string representation of the cards object for printing
    def __str__(self):
        str = ''
        for card in self.cards:
            str += "{:>3}, ".format(card)
        return str[:-2]

    # add_deck    ->  One optional argument to specify adding more than one 52
    #                 card deck to the cards
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
    def add_joker(self, jokers = 1):
        # For the number of jokers specified, add a joker to the top of the pile
        for i in range(jokers):
            self.cards.append('J')
    
    # shuffle     ->  Randomly shuffle the cards
    def shuffle(self):
        random.shuffle(self.cards)

    # sort        ->  Arrange the cards in order by suit, one argument that
    # specifies whether you like the values right to left 'rtl' default, or left
    # to right 'ltr', otherwise known as reverse order for pagans
    #
    # TODO: After doing it, I realized there are better ways. It works so I'm
    # leaving it for now, but I will rewrite it to use filter and map instead of
    # needing to sort many different times
    def sort(self, direction='rtl'):
        # First we need to sort the cards by suit
        self.cards.sort(key=Cards.suit_key)

        # Now, we need to sort each suit by number
        # Create the boundaries of each suit to slice
        s1 = 1 if 'J' in self.cards else 0
        s2 = s1 + self.spades()
        s3 = s2 + self.hearts()
        s4 = s3 + self.clubs()

        # Sort spades
        sorted_spades = sorted( self.cards[s1:s2], key=Cards.value_key,
            reverse = False if direction is 'ltr' else True)

        # Sort hearts
        sorted_hearts = sorted( self.cards[s2:s3], key=Cards.value_key,
            reverse = False if direction is 'ltr' else True)

        # Sort clubs
        sorted_clubs = sorted( self.cards[s3:s4], key=Cards.value_key,
            reverse = False if direction is 'ltr' else True)

        # Sort the fourth suit
        sorted_diamonds = sorted( self.cards[s4:], key=Cards.value_key,
            reverse = False if direction is 'ltr' else True)
        
        # Combine the suits in an order depending on what suits are had
        if self.spades() and self.hearts() and self.clubs():
            self.cards = (sorted_spades + sorted_hearts + sorted_clubs
                + sorted_diamonds)

        elif not self.hearts():
            self.cards = sorted_spades + sorted_diamonds + sorted_clubs

        elif not self.clubs():
            self.cards =  sorted_hearts + sorted_spades + sorted_diamonds

        # Add the Joker back in if it was in hand
        if s1:
            self.cards.insert(0, 'J')

    # These properties all return the number of the suit in a hand
    # The property decorator means no parentheses needed when called
    def spades(self):
        return len(list(filter(lambda x: True if x[-1] is 'S' else False,
        self.cards)))
    def hearts(self):
        return len(list(filter(lambda x: True if x[-1] is 'H' else False,
        self.cards)))
    def clubs(self):
        return len(list(filter(lambda x: True if x[-1] is 'C' else False,
        self.cards)))
    def diamonds(self):
        return len(list(filter(lambda x: True if x[-1] is 'D' else False,
        self.cards)))

    @staticmethod
    def suit_key(card):
        return {'J':0, 'S':1, 'H':2, 'C':3, 'D':4}[card[-1]]

    @staticmethod
    def value_key(card):
        return {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '1':8,
        'J':9, 'Q':10, 'K':11, 'A':12}[card[0]]

    # deal        ->  remove cards from the top of the pile and add the removed
    #                 card to a new hand, then return a tuple of the amount of
    #                 hands that were specified. Deal the number of cards
    #                 specified by hand_size
    def deal(self, hands, hand_size):
        # Create an empty tuple of size hands
        dealt_hands = tuple(Cards() for i in range(hands))
        # For the number of cards to be dealt per hand
        for i in range(hand_size):
            # Put the top card from the deck into each hand
            for j in range(hands):
                dealt_hands[j].cards.append(self.cards.pop())
        return dealt_hands
