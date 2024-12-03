import pygame, sys, manager
import objects.images
import objects.movable
import objects.enemy 
import objects.buttons





def output(window): 
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/gamebgg.png")  #images in objects 
    btn_back=objects.buttons.with_images(670, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(730,10, 40,40,"images/exit.png", "images/exit(2).png")
    kelp= objects.images.animated(760,440,40,40,"images/seaweed.gif",50) 
    kelp=objects.images.animated(40,440,40,40,"images/seaweed.gif",50) 
    run = True
    pygame.display.set_caption("GAME")


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

    



    while run:
        window.fill((255,255,255))
        bg.draw(window)
        btn_back.draw(window)
        btn_exit.draw(window)
        kelp.draw(window)
       
       
       
        for event in pygame.event.get(): 
           if btn_back.update(pygame.mouse.get_pos(),event):
                manager.level=0
                run=False #should not run or continue
           if btn_exit.update(pygame.mouse.get_pos(),event):
               sys.exit()
           
           
           if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw