import objects.images 

class moving(objects.images.still):
    def __init__(self, x,y, width, height, images_to_use, speed ):
        super().__init__( x,y, width, height, images_to_use)
        self.speed= speed
    


     #enemies will swim back and forth, not up or down. We want them to be in different locations and maybe not timed up, so we'll have to see 
     # one: how to make them generate in different locations (probs in def spawn) and two: how to make it so that they all don't start changing direction as soon as one touches the wall
     # (probably a for every in enemuy list or something idk)

    def spawn(self):
        enemies = [] #look at this agin later cuase I'm not too sure how well that is, I think for math for enemy location
        # could totally copy from the 2d list program
        if len(enemies) < 4:
            enemies.append(objects.images.still(0,0,100,100,"images/"))
        
        health = 3
        
        if health<=0:
            pass

    def swim_right (self):
        self.rect.x  += self.speed
    
    def swim_left(self):
        self.rect.x  -= self.speed 

    def attack(self, diver):
        pass
    # Don't know how to do this yet, also not sure whether or not def attack will also take damage off of enemy or if we need a separate def
    