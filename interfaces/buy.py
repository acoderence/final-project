import pygame, sys, manager, objects.buttons



def output(window): 
    
    run = True
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    
    
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
        window.fill((217, 186, 137))#tan backround. feels very shop-like idk
        gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)#grid
        btn_exit.draw(window)
        btn_back.draw(window)

    while run == True:
        display()
       
       
        for event in pygame.event.get(): 
            if btn_exit.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = -1
            
            if btn_back.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 5
           
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw