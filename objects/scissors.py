import pygame,sys
import objects.diver
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
    
    
    
    #run = True   
    #while run: 
          #attack_count+=1
        
    
        
   #  def hit(self):
        
         #key_input = pygame.key.get_pressed()
       #scissors being thrown by the diver...attacks enemy for sure but cuts seaweed maybe
         #if key_input[pygame.K_SPACE] and attack_count>50:
            #attack.append(objects.diver.move(self.rect.x,self.rect.y, 40, 40,"images/scissors.png",20))
            #attack_count=0
            #pass
             
         
        
    
        
 