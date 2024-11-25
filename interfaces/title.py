import pygame, sys, manager


def output(window): 
    
    run = True

    def display():
        window.fill((94, 188, 224))#fills white window, pretty basic

    while run == True:
       
       
       
        for event in pygame.event.get(): 
           
           
           if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw