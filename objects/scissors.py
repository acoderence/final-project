import pygame,sys
import objects.diver
import objects.enemy
import objects.images
import manager
import objects.movable

#scissors can be used to cut seaweed/kelp and used to attack enemies
#


class cut(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
    
    
    
    def hit(self):
       key_input = pygame.key.get_pressed()
       self.movex = (key_input[pygame.K_SPACE] * -self.speed) + (key_input[pygame.K_SPACE] * self.speed)
     
        
 