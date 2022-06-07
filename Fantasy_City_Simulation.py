import numpy as np
import random

print("Hello World")

print("did my push work?")

food = [1]*10

class Citizen:
    def __init__(self, l):
        self.strength = l[0]
        self.dex = l[1]
        self.con = l[2]
        self.int = l[3]
        self.wis = l[4]
        self.cha = l[5]
        self.l= l

def growth(c1,c2,x):
    return Citizen(list(c1.l[0:x] + c2.l[x:len(c1.l)]))
    


l = [10,12,8,10,12,8]

c1 = Citizen(l)

l = [11,11,11,11,11,11]

c2 = Citizen(l)

random.randint(0, 5)

c3 = growth(c1,c2,random.randint(0, 5))

c3.l