import pygame, sys, manager
import objects.buttons
import objects.text
import objects.images



def output(window):
    font = pygame.font.SysFont('Consoles',35) 
    help_text = objects.images.animated(100,30,300,300,"images/helptext.gif",50) 
    bg= objects.images.animated(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/help(3).gif",100)  #images in objects 
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    arrows= objects.images.still(110,300, 105,105, "images/keypress.png")
    spacebar=objects.images.still(300,230,150,150, "images/spacebar.png")
    run = True
    pygame.display.set_caption("HELP")
    
   



    while run:
       window.fill((255,255,255))
       bg.draw(window)
       bg.update()
       help_text.draw(window)
       help_text.update()
       btn_back.draw(window)
       btn_exit.draw(window)
       arrows.draw(window)
       spacebar.draw(window)
       #help_msg=" How To Play:\n Press arrow keys to MOVE around and space bar to COLLECT tresure to sell to the Seaside Merchant for new equipment when you resurface"
       #objects.text.blit_text(window,help_msg,(100,100),font)
       
       
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