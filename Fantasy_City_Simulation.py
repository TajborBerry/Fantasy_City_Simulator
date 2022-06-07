import numpy as np
import random

print("Hello World")

print("did my push work?")

food = [1]*10

class Citizen:
    def __init__(self, l):
        self.str = l[0]
        self.dex = l[1]
        self.con = l[2]
        self.int = l[3]
        self.wis = l[4]
        self.cha = l[5]
        self.l= l       
    def statblock(self):
        print(" Strength: " + str(self.str) 
        + "\n Dexterity: " + str(self.dex)
        + "\n Constituion: " + str(self.con)
        + "\n Intelligence: " + str(self.int)
        + "\n Wisdom: " + str(self.wis)
        + "\n Charisma: " + str(self.cha))

def growth(c1,c2,x):
    return Citizen(list(c1.l[0:x] + c2.l[x:len(c1.l)]))

    


l = [10,12,8,10,12,8]

c1 = Citizen(l)

l = [11,11,11,11,11,11]

c2 = Citizen(l)

random.randint(0, 5)

c4 = growth(c1,c2,random.randint(0, 5))

c4.l

list1 = [1, 2, 3]
list2 = [4, 5, 6]

products = [a * b for a, b in zip(list1, list2)]