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

def growth(c1,c2):
    indices = random.sample(range(len(c1.l)),int(len(c1.l)/2))
    newpeepo = c1.l.copy()
    for i in range(int(len(c1.l))):
        if i in indices:
            newpeepo[i]= c2.l[i]
    return Citizen(newpeepo)


def growth_old(c1,c2,x):
    return Citizen(list(c1.l[0:x] + c2.l[x:len(c1.l)]))



l = [10,12,8,10,12,8]

c1 = Citizen(l)

l = [11,11,11,11,11,11]

c2 = Citizen(l)

random.randint(0, 5)

c3 = growth_old(c1,c2,random.randint(0, 5))
c3.l

c4 = growth(c1,c2)
c4.l


'''

Learning material

'''

'''
two list multiplication
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

products = [a * b for a, b in zip(list1, list2)]