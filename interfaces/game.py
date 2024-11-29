import pygame, sys, manager
import objects.images
import objects.movable
import objects.enemy 
import objects.buttons





def output(window): 
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.animated(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"iamges/gamebg.jpg")  #images in objects 
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    run = True
    pygame.display.set_caption("GAME")

    



    while run:
        window.fill((255,255,255))
        bg.draw(window)
        btn_back.draw(window)
        btn_exit.draw(window)
       
       
       
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