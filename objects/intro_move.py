import pygame
import objects.images 

#this here is pretty much just like the normal moving file but the player can't go up or down. 
class movable(objects.images.still):
    def __init__(self, x,y, width, height, images_to_use, speed):
        super().__init__( x,y, width, height, images_to_use)
        self.speed= speed
        
    def key_press(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] * -self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        
    
        self.rect.x += self.movex
        
    
    def back(self):
        self.rect.x -= self.movex
        