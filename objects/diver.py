import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

class move(objects.images.animated): ##check
    def __init__(self, x, y,width,height,image_to_use,speed,update):
        super().__init__(x, y,width,height, image_to_use,update)
        self.speed = speed
 
 
    def movement(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] *-self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.movey = (key_input[pygame.K_UP] *-self.speed) + (key_input[pygame.K_DOWN] * self.speed) 
        
        self.rect.x+= self.movex
        self.rect.y+= self.movey
        
        
    
  
     
     
    
    oxygen_timer=60
    enemiess=[]
    oxygen=50
     
    


   

    def health(self,window,oxygen):
        #health bar and oxygen combined
        pygame.draw.rect(window, (99, 217, 15),(self.rect.x +20, self.rect.y+90,oxygen, 10))# creates health/oxygen bar under diver
        #for x in enemies:
        # if pygame.sprite.collide_mask(x , self): ###redo this
          #oxygen=oxygen-10
      
         

    

    def borders(self):
        pass #the if statments below were erroring so I tried to tab them into the borders def but then the diver variable couldn't be recognized so I just made it pass so it wouldn't error
            #borders for diver
        if self.rect.x<0:
           self.rect.x=0
          
        if self.rect.y<0:
           self.rect.y=0
            #display()
        if self.rect.x>400:
             self.rect.x=400
            # display()
        if self.rect.y>400:
            self.rect.y=400
            # display()

    def attacks(self):
       pass