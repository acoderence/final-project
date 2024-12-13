import pygame, sys

#hopefully, when treasure gets picked up, it will be added to the list. And the list has a max. The max get bigger as the bag upgrades, num
# stands for number in the database (which I will add later, it hopefully should keep track of what upgrae player is on per account) and depending on 
# the num/upgrade the max increases (we only have the base and first upgrade but until we make sure this works lets not add more)
def storage (treasure,num):
    inventory = []
    done = 0
    #bag 1
    max = 5+(int(num) * 5 )
    
    if len(inventory) < int(max):
        inventory.append  (treasure)
        done = 1
    elif len(inventory) >= int(max):
        done= -1
    
    
    