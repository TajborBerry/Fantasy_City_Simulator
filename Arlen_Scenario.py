#importing a package called random, which handles random number generation
import random 

#creating an empty list so I can append values to it later
ered= []

#run the below algorithm 10 million times
for i in range(10000000):
    sum=0 #the value of variable sum is 0, so every 30 rolls are going to be starting from 0
    for k in range(30): #do the below algorithm 30 times
        sum += random.randint(1, 8) #roll a d8 and add it's value to sum
    ered.append(sum) #after rolling 30 times add the rolles values summ to list ered

alive_ered = [x for x  in ered if x<48] #creating a new list from the ered list when he stays alive (sum value is below 48)
len(alive_ered) #0

notdead_ered = [x for x  in ered if x<96] #creating a new list from the ered list when we have a chance to save (sum value is below 96)
len(notdead_ered) #7100