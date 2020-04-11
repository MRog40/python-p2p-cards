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

"""
"""

from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time


#Start Alice's direct server.
alice_dht = DHT()
alice_direct = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2", net_type="direct", dht_node=alice_dht, debug=1)
alice_direct.start()

#Start Bob's direct server.
bob_dht = DHT()
bob_direct = Net(passive_bind="192.168.0.44", passive_port=44445, interface="eth0:1", net_type="direct", node_type="active", dht_node=bob_dht, debug=1)
bob_direct.start()

#Callbacks.
def success(con):
    print("Alice successfully connected to Bob.")
    con.send_line("Sup Bob.")

def failure(con):
print("Alice failed to connec to Bob\a")

events = {
    "success": success,
    "failure": failure
}

#Have Alice connect to Bob.
alice_direct.unl.connect(bob_direct.unl.construct(), events)

#Event loop.
while 1:
#Bob get reply.
for con in bob_direct:
    for reply in con:
        print(reply)

#Alice accept con.
for con in alice_direct:
    x = 1

time.sleep(0.5)
