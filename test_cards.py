from mighty import *

me = player('Michael')

table = mighty_tabl('Table 1')

#table.hand.add_deck()
table.hand.add_joker()
table.hand.shuffle()

print(table)

(me.hand,) = table.hand.deal(1, 26)

me.hand.sort()

print(me)
me.hand.add_deck()
print(table)
print(me)

