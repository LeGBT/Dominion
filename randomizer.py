#!/usr/local/bin/python3

from sys import argv
from random import random

requiregold = 0

if len(argv) > 1:
    reset = (argv[1] == "--reset")
else:
    reset = 0

cards = {}
with open("cartes") as f:
    for line in f:
        l = line.split()
        nom = l[0]
        valeurs = l[1:]
        if nom != "#":
            cards[nom] = [int(i) for i in valeurs]

# copies des prix
prices = {}
for c in cards:
    prices[c] = cards[c][1]



if requiregold:
    for c in cards:
        if cards[c][2]:
            prices[c] *= 13
        else:
            prices[c] *= 10

# pondérer de 0.8 par les dernières sorties :
if not reset:
    for c in cards:
        prices[c] = int(10*0.8**cards[c][0]*prices[c])
else:
    print("===== Old card count reseted! ====\n")
    for c in cards:
        cards[c][0] = 0


def getfrep(cards):
    frep = []
    s = 0
    for c in cards.keys():
        s += prices[c]
        frep.append(s)
    return frep

res = set()

frep = getfrep(cards)
# print(frep)
s = sum([prices[c] for c in cards])
while len(res) < 10:
    r = random()*s
    i = 0
    while frep[i] < r:
        i += 1
    res.add(list(cards.keys())[i])

for c in sorted(res):
    print(c)

# on met à jour le nombre de sorties des cartes
for c in cards:
    if c in res:
        cards[c][0] += 1
    else:
        cards[c][0] = 0

def merge(l, s):
    if l:
        return merge(l[1:], s+str(int(l[0]))+" ")
    else:
        return s

newcardlist = ""
for c, v in cards.items():
    newcardlist += c
    newcardlist += " "
    newcardlist += merge(v, "")
    newcardlist += "\n"


with open("cartes", "w") as f:
    f.write(newcardlist)




