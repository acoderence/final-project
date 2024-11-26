import pygame, sys, manager
import objects.buttons
import objects.text
import objects.images



def output(window):
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/helpbg.jpg")  #images in objects 
    btn_back=objects.buttons.with_images(100, 100, 350,30,"images/back.png, images/back(2).png")
    btn_exit= objects.buttons.with_images(100, 100, 400,30,"images/exit.png, images/exit(2).png")
    arrows= objects.images.still(100,230, 150,150, "images/keypress.png")
    spacebar=objects.images.still(100,300,150,150, "images/creditbg.png")
    run = True
    pygame.display.set_caption("HELP")
    
   



    while run:
       window.fill((255.255,255))
       bg.draw(window)
       btn_back.draw(window)
       btn_exit.draw(window)
       arrows.draw(window)
       spacebar.draw(window)
       help_msg=" How To Play:\n Press arrow keys to MOVE around and space bar to COLLECT tresure to sell to the Seaside Merchant for new equipment when you resurface"
       objects.text.blit_text(window,help_msg,(100,100),font)
       
       
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