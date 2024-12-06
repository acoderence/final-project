import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

class kill(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
 
  
def output(window): 
    global oxygen 
    diver=(objects.movable.movable(200,380,100,100,"images/diver.gif",5))
   
     
    oxygen=50
     
     
    def gridHelp(window,WINDOW_WIDTH, WINDOW_HEIGHT):#just the grid as always
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY))     
     


    def display():
        global oxygen
        diver.draw(window)
        window.fill((255,255,255))
  
     
        #health bar and oxygen combined
        pygame.draw.rect(window, (255,255,255),(diver.rect.x +20, diver.rect.y+100,oxygen, 10))# creates health/oxygen bar under diver
    if pygame.sprite.collide_mask(objects.enemy, diver ): ###redo this
          health=health-10
      
         

    diver.key_press()
    display()

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


#attacks
#key_input = pygame.key.get_pressed()
 #    if key_input[pygame.K_SPACE]



   

 