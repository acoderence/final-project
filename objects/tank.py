import pygame, sys 
    
import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

class air(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
    
    
    
   # def draw_timer():
        #timer_text=window.blit(font.render(f"")