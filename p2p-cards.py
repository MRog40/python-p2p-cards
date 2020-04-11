import pyp2p
from mighty import *


me = player('Michael')
p1 = player('p1')
p2 = player('p2')
p3 = player('p3')
p4 = player('p4')

table = mighty_table()

table.deck.add_deck()
table.deck.add_joker()
table.deck.shuffle()

(p1.hand, p2.hand, p3.hand, p4.hand, me.hand) = table.deck.deal(5, 10)

print("Players and their hands:")
print(p1)
print(p2)
print(p3)
print(p4)
print(me)

