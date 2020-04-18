#import pyp2p
from mighty import *

me = Player('Michael')
p1 = Player('Layne')
p2 = Player('Andrew')
p3 = Player('Theo')
p4 = Player('Ashley')

table = MightyTable()

table.deck.add_deck()
table.deck.add_joker()
table.deck.shuffle()


(p1.hand, p2.hand, p3.hand, p4.hand, me.hand) = table.deck.deal(5, 10)

p1.hand.sort()
p2.hand.sort()
p3.hand.sort()
p4.hand.sort()
me.hand.sort()

print("Players and their hands:")
print(p1)
print(p2)
print(p3)
print(p4)
print(me)
print(table)

