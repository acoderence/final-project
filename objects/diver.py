import pygame,sys
import objects.images
import manager
import objects.movable

class kill(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
 
  
    def output(window): 
     diver=(objects.movable.movable(200,380,100,100,"images/diver.gif",5))
     run = True



     def display():

      while run:
        diver.draw(window)


        diver.key_press()
        display()

            #borders for objects
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


#attacks
#key_input = pygame.key.get_pressed()
 #    if key_input[pygame.K_SPACE]



   

 