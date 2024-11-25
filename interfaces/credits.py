import pygame, sys
import manager
import objects.buttons
import objects.text
import objects.images
pygame.init()




    
def output(window):
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"")  #images in objects 
    btn_back=objects.buttons.with_images(100, 100, 350,30,"images/back.png, images/back(2).png")
    btn_exit= objects.buttons.with_images(100, 100, 400,30,"images/exit.png, images/exit(2).png")
    run = True
    pygame.display.set_caption("CREDITS")




    while run:
        #display()
        window.fill((255,255,255))
        bg.draw(window)
        btn_back.draw(window)
        btn_exit.draw(window)
        credits_msg="DEEP SEA DIVER\nDeveloped by: Abbigail Spence and Brianna Wright Special \nThanks:Markus Notch Perrson Copyright 2024 Thank You For Playing"
        objects.text.blit_text(window,credits_msg,(100,240),font)







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
    
       
