import numpy as np
import random

class Citizen:
    def __init__(self, l, parent = "God", FirstName = "Cool" , FamilyName = "Gang" ):
        self.str = l[0]
        self.dex = l[1]
        self.con = l[2]
        self.int = l[3]
        self.wis = l[4]
        self.cha = l[5]
        self.l= l
        self.childlist = []
        self.parent = parent
        self.FirstName = FirstName
        self.FamilyName = FamilyName
        self.partner = None
        self.relationship = False
        self.married = False
    def statblock(self):
        print(" Strength: " + str(self.str) 
        + "\n Dexterity: " + str(self.dex)
        + "\n Constituion: " + str(self.con)
        + "\n Intelligence: " + str(self.int)
        + "\n Wisdom: " + str(self.wis)
        + "\n Charisma: " + str(self.cha))
    def childlistadd(self,child):
        self.childlist.append(child)
    def __str__(self):
        return str(self.FirstName)+ " " + str(self.FamilyName)
    def print(self):
        return str(self.FirstName)+ " " + str(self.FamilyName)
    def selectmate(self,c1,married = False):
        self.partner = c1
        c1.partner = self
        self.Relationship = True
        c1.Relationship = True
        if married:
            self.married = True
            c1.married = True
    def mating(self,c1):
        if self.Relationship:
            indices = random.sample(range(len(c1.l)),int(len(c1.l)/2))
            newpeepo = c1.l.copy()
            for i in range(int(len(c1.l))):
                if i in indices:
                    newpeepo[i]= c2.l[i]
            child = Citizen(newpeepo,parent=[c1.print(),c2.print()])        
            self.childlistadd(child)
            c1.childlistadd(child)
            return child





l = [10,12,8,10,12,8]

c1 = Citizen(l,FirstName= "David", FamilyName= "Uhg")

l = [11,11,11,11,11,11]

c2 = Citizen(l,FirstName= "Daniella", FamilyName= "Guh")

random.randint(0, 5)

c3 = mating_old(c1,c2,random.randint(0, 5))
c3.l

c4 = mating(c1,c2)
c4.l

c1.childlistadd(c4.print())
c2.childlistadd(c4.print())




'''

Learning material

'''

'''
two list multiplication
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

products = [a * b for a, b in zip(list1, list2)]



'''
Old outdated stuff
'''
def mating(c1,c2):
    indices = random.sample(range(len(c1.l)),int(len(c1.l)/2))
    newpeepo = c1.l.copy()
    for i in range(int(len(c1.l))):
        if i in indices:
            newpeepo[i]= c2.l[i]
    return Citizen(newpeepo,parent=[c1.print(),c2.print()])


def mating_old(c1,c2,x):
    return Citizen(list(c1.l[0:x] + c2.l[x:len(c1.l)]))