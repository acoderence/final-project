import pygame, sys
import manager
import objects.buttons
import objects.text
import objects.images
pygame.init()




    
def output(window):
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.animated(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/creditbg(2).gif", 50)  #images in objects 
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    run = True
    pygame.display.set_caption("CREDITS")




    while run:
        #display()
        window.fill((255,255,255))
        bg.draw(window)
        bg.update()
        btn_back.draw(window)
        btn_exit.draw(window)
        credits_msg="DEEP SEA DIVER\nDeveloped by: Abbigail Spence and Brianna Wright  \nSpecial Thanks:Markus Notch Perrson \nCopyright 2024 \nThank You For Playing"
        objects.text.blit_text(window,credits_msg,(100,100),font,((255,255,255)))







        for event in pygame.event.get():   



            if btn_back.update(pygame.mouse.get_pos(),event):
                manager.level=0
                run=False #should not run or continue
            if btn_exit.update(pygame.mouse.get_pos(),event):
               sys.exit()

           

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #download pip install
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw 
    
       
