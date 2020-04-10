import p2p
from mighty import *


me = player('Michael')

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

