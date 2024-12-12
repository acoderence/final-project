import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text, objects.movable


def output(window): 
    
    run = True
    
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    btn_buy = objects.buttons.with_images(40, 390, 180,120,"images/buy_1.png", "images/buy_2.png")
    btn_sell = objects.buttons.with_images(300, 390, 180,120,"images/sell_1.png", "images/sell_2.png")
    font = pygame.font.SysFont('Consolas', 30)
    font2 = pygame.font.SysFont('Consolas', 25)
    text = "Hey! Welcome \nto my shop!" 
    merchant = objects.images.still(0,0,500,500,"images/merchant.png")
    bubble = objects.images.still(-30,-10,360,180,"images/bubbly.png")
    money_display = f"{manager.money}"
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
        merchant.draw(window)
        #gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT) #grid
        
        btn_exit.draw(window)
        btn_back.draw(window)
        btn_buy.draw(window)
        btn_sell.draw(window)
        bubble.draw(window)
        
        objects.text.blit_text(window,text,(30,30,),font)
        objects.text.blit_text(window,money_display,(340,350,),font2)
    while run == True:
        display()
        
        for event in pygame.event.get():
            
            display()
            
            if btn_exit.update(pygame.mouse.get_pos(),event):
                run = False
                pygame.quit()
                sys.exit()
            
            if btn_back.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 4
            if btn_buy.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 6
            if btn_sell.update(pygame.mouse.get_pos(),event):
                pass
           
                
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw