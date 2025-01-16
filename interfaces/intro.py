import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text, objects.intro_move
#Kind of like a lobby where players can choose to either play the game or go to sell or buy 
def output(window): 
    
    run = True
    #image creation pretty much
    beach = objects.images.still(0,-20, 800, 800, "images/beach.jpg")
    border = objects.images.still(-800,0, 800, 800, "images/beach.jpg")
    dock = objects.images.still(-40,350, 900, 200, "images/dock.png")   
    hut = objects.images.still(370,120, 300, 300, "images/hut.png")   
    sign = objects.images.still(0,290, 120, 100, "images/sign.png")  
    shop_open= objects.images.still(370,120, 300, 300, "images/hut_open.png")  
    birds=objects.images.animated(60,40,100,100,"images/flyingbirds.gif",100)
    seagull=objects.images.still(430,117,45,45,"images/seagull.png")
    #player
    player = objects.intro_move.movable(190,260,120,180, "images/placer.png",6)
    #buttons
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    
    #Text stuff
    font = pygame.font.SysFont('Consolas', 30)
    text = "Dive" 
    
    def gridHelp(window,WINDOW_WIDTH, WINDOW_HEIGHT):#just the grid again
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
        window.fill((255,255,255))#fills white window, pretty basic, it gets covered by an image anyways
        #background image
        beach.draw(window)
        birds.draw(window)
        birds.update()
        seagull.draw(window)
        seagull.update()
        #gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT) #grid
        #draws images
        border.draw(window)
        dock.draw(window)
        hut.draw(window)
        sign.draw(window)
        #text draw
        objects.text.blit_text(window,text,(20,310,),font)
        #player draw
        player.draw(window)
        #button draw
        btn_exit.draw(window)
        btn_back.draw(window)
        #makes it so that if the player is within a certain distance of the hut it opens it's doors. I thought the idea was cute
        if player.rect.x > 210:
            shop_open.draw(window)
        
        
        
    while run == True:
        display()
        #moves the player
        player.key_press() 
        
        if pygame.sprite.collide_mask(player, hut):#if player runs into the hut image, it teleports them to merchant page
            player.back()
            run = False
            manager.level = 5
        if pygame.sprite.collide_mask(player, border):#if the player runs into the border image (which is just off screen) they get teleported to game
            player.back()
            run = False
            manager.level= 3
        for event in pygame.event.get():
            
            display()
            if btn_exit.update(pygame.mouse.get_pos(),event):#exits
                 sys.exit()
            
            if btn_back.update(pygame.mouse.get_pos(),event):#goes back
                run = False
                manager.level = 0
           
                
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw