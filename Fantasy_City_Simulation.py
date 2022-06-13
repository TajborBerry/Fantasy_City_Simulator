import numpy as np
import random
import names

class Citizen:
    def __init__(self, l, parent = "God", FirstName = "Kurt" , FamilyName = "Coban", gender = "female"):
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
        self.gender = gender
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
        self.relationship = True
        c1.relationship = True
        if married:
            self.married = True
            c1.married = True
    def mating(self,c1):
        if self.relationship:
            indices = random.sample(range(len(c1.l)),int(len(c1.l)/2))
            newpeepo = c1.l.copy()
            for i in range(int(len(c1.l))):
                if i in indices:
                    newpeepo[i]= self.l[i]
            child = Citizen(newpeepo,parent=[c1.print(),self.print()], FamilyName = self.FamilyName)        
            self.childlistadd(child)
            c1.childlistadd(child)
            return child


def random_citizen(femaleprop = 0.5):
    mu, sigma = 10, 1 # mean and standard deviation
    l = np.random.normal(mu, sigma, 6)
    l = [round(x) for x in l]
    if random.random() < femaleprop:
        gender = "female"
    else:
        gender = "male"
    FirstName = names.get_first_name(gender=gender)
    FamilyName = names.get_last_name()
    citizenlist.append(Citizen(l,FirstName= FirstName, FamilyName= FamilyName))
    


citizenlist = []
l = [10,12,8,10,12,8]

c1 = Citizen(l,FirstName= "David", FamilyName= "Duhlo")

l = [11,11,11,11,11,11]

c2 = Citizen(l,FirstName= "Daniella", FamilyName= "Weiler")
citizenlist = [c1,c2]

[print(x.gender) for x in citizenlist]

def creating_citizen():
    l=[]
    l.append(input("Enter strength:"))
    l.append(input("Enter dexterity:"))
    l.append(input("Enter constitution:"))
    l.append(input("Enter intelligence:"))
    l.append(input("Enter wisdom:"))
    l.append(input("Enter charisma:"))
    FirstName= input("Enter First Name:")
    FamilyName= input("Enter Last Name:")
    citizenlist.append(Citizen(l,FirstName= FirstName, FamilyName= FamilyName))



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


random.randint(0, 5)

c3 = mating_old(c1,c2,random.randint(0, 5))
c3.l

c4 = mating(c1,c2)
c4.l

c1.childlistadd(c4.print())
c2.childlistadd(c4.print())

'''
global vs local variable
'''

x = "olo"
def myfunc():
    global x
    x = "lol"
    print(x)


mu, sigma = 10, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 6)
s = [round(x) for x in s]


import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()