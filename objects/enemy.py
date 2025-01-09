import objects.images, pygame, sys





class moving(objects.images.still):
    def __init__(self, x,y, width, height, images_to_use, speed, health, damage):
        super().__init__( x,y, width, height, images_to_use)
        self.speed= speed
        self.health = health
        self.damage = damage
    def swim(self):
        self.rect.x  += self.speed
    
    def hurt(self):
        self.health = self.health - self.damage
        

    
    
    