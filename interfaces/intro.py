import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text, objects.movable


def output(window): 
    
    run = True
    beach = objects.images.still(0,-20, 800, 800, "images/beach.jpg")
    dock = objects.images.still(-40,350, 900, 200, "images/dock.png")   
    hut = objects.images.still(370,120, 300, 300, "images/hut.png")   
    sign = objects.images.still(0,290, 120, 100, "images/sign.png")   
    player = objects.movable.movable(190,260,120,180, "images/placer.png",6)
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    shop_open= objects.images.still(370,120, 300, 300, "images/hut_open.png")  
    font = pygame.font.SysFont('Consolas', 30)
    text = "Dive" 
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
        objects.text.blit_text(window,text,(20,310,),font)
        player.draw(window)
        btn_exit.draw(window)
        btn_back.draw(window)
        if player.rect.x > 210:
            shop_open.draw(window)
        
        
        
    while run == True:
        display()
        player.key_press() 
        if pygame.sprite.collide_mask(player, hut):
            player.back()
            run = False
            manager.level = 4
        if player.rect.x < sign.rect.x:
            player.back()
            run = False
            manager.level= 3
        for event in pygame.event.get():
            
            display()
            
            if btn_exit.update(pygame.mouse.get_pos(),event):
                run = False
            
            if btn_back.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 0
           
                
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw