import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

#scissors can be used to cut seaweed/kelp and used to attack enemies
#
attack=[]

class cut(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
        
attack_count=50       
        
def hit():
        
         key_input = pygame.key.get_pressed()

         if key_input[pygame.K_SPACE] and attack_count>50:
            attack.append(objects.player.kill(diver.rect.x,dievr.rect.y, 40, 40,"images/catnip.png",20))
            attack_count=0
            
         
        
        
        
 