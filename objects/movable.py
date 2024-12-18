import pygame
import objects.images 

class movable(objects.images.still):
    def __init__(self, x,y, width, height, images_to_use, speed):
        super().__init__( x,y, width, height, images_to_use)
        self.speed= speed
        
    def key_press(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] * -self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.movey = (key_input[pygame.K_UP] * -self.speed) + (key_input[pygame.K_DOWN] * self.speed)
        #self.movex = (key_input[pygame.K_SPACE] * -self.speed) + (key_input[pygame.K_SPACE] * self.speed)
        
        self.rect.x += self.movex
        self.rect.y += self.movey
    
    def back(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey