import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text

manager.WINDOW_WIDTH = 800
def output(window): 
    
    run = True
    beach = objects.images.still(0,-20, 800, 800, "images/beach.jpg")
    dock = objects.images.still(10,350, 900, 200, "images/dock.png")   
    hut = objects.images.still(670,120, 300, 300, "images/hut.png")   
    sign = objects.images.still(50,290, 120, 100, "images/sign.png")   
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
        window.fill((255,255,255))#fills white window, pretty basic
        beach.draw(window)
        gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT) #grid
        dock.draw(window)
        hut.draw(window)
        sign.draw(window)
    while run == True:
        display()
       
       
        for event in pygame.event.get(): 
            
        
          
            
                
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw