import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

class move(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
 
 
    def movement(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] *-self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.movey = (key_input[pygame.K_UP] *-self.speed) + (key_input[pygame.K_DOWN] * self.speed) 
        self.rect.x+= self.movex
        self.rect.y+= self.movey
        
         
         
  
     
     
    diver=(objects.movable.movable(200,380,100,100,"images/diver.gif",5)) #PLACE ON GAME SCREEN
   
     
    oxygen=50
     
    


    def display():
        global oxygen
        window.fill()

    def health(self):
        #health bar and oxygen combined
        pygame.draw.rect(window, (255,255,255),(diver.rect.x +20, diver.rect.y+100,oxygen, 10))# creates health/oxygen bar under diver
        if pygame.sprite.collide_mask(objects.enemy, diver ): ###redo this
          health=health-10
      
         

    diver.key_press()
    display()


    def borders(self):
            #borders for diver
    if diver.rect.x<0:
         diver.rect.x=0
         display()
    if diver.rect.y<0:
        diver.rect.y=0
        display()
    elif diver.rect.x>400:
         diver.rect.x=400
         display()
    elif diver.rect.y>400:
         diver.rect.y>400
         display()

    def attacks(self):
        