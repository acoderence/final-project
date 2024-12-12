import sqlite3,pygame,sys
import objects.images
import objects.movable
import objects.buttons
import manager
import objects.bag as bag
import random


treasure=[]

class gems(objects.images.still): 
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
  


#create treasure at random position
    for in range(10):
        treasure= treasure(random.randint)
        pass 
        
    

#I'm not sure if this will work but hopefully if a treasure is collected, it will add a value to the bag inventory so we can add it up later. this system
#makes it so that all treasure has the same value but if we can get it working then we can adjust that later. 
def collect(diver,treasure):

    if pygame.sprite.collide_mask(diver, treasure):
        bag.inventory.append(int(80))
        
def draw():
    pass