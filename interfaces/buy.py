import pygame, sys, manager, objects.buttons, objects.text



def output(window): 
    
    run = True
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    money = "0"
    font = pygame.font.SysFont('Consolas', 25)
    btn_buy1 = objects.buttons.with_images(40, 100, 180,120,"images/upgrade_1.png", "images/upgrade_2.png")
    btn_buy2 = objects.buttons.with_images(40, 200, 180,120,"images/upgrade_1.png", "images/upgrade_2.png")
    btn_buy3 = objects.buttons.with_images(40, 390, 180,120,"images/upgrade_1.png", "images/upgrade_2.png")
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
        btn_buy1.draw(window)
        btn_buy2.draw(window)
        btn_buy3.draw(window)
        objects.text.blit_text(window,money,(340,350,),font)
    while run == True:
        display()
       
       
        for event in pygame.event.get(): 
            if btn_buy1.update(pygame.mouse.get_pos(),event):
                pass
            if btn_buy2.update(pygame.mouse.get_pos(),event):
                pass
            if btn_buy3.update(pygame.mouse.get_pos(),event):
                pass
                    
            if btn_exit.update(pygame.mouse.get_pos(),event):
                run = False
                pygame.quit()
                sys.exit()
            
            if btn_back.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 5
           
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw