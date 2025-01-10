import objects.images, pygame, sys





class moving(objects.images.still):
    def __init__(self, x,y, width, height, images_to_use, speed, health, damage):
        super().__init__( x,y, width, height, images_to_use)
        self.speed= speed 
        self.health = health
        self.damage = damage
    def swim(self): #makes enemy swim based on given value from the game screen
        self.rect.x  += self.speed
    
    def hurt(self):#health and damage gets given a value from game screen, and here, the max enemy health subtracts the damage done by player. 
        #this is how we keep track of each of the enemies health. 
        self.health = self.health - self.damage
        

    
    
    