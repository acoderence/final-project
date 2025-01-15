import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text, objects.movable


def output(window): 
    
    run = True
    #connects to database
    connection = objects.data_stuff.create_connection('player_account.db')
    #connects to the username that is signed in (using variables from manager page)
    result = objects.data_stuff.select_db(connection,"player_account",[f"username ='{manager.account_user}'",f"password='{manager.account_pass}'"]).fetchall() 
    #takes necessary values from the result list that is needed for selling function, and gives it a variable that I can use later
    for i in result:
        account_id = int(i[0])
        account_inventory = int(i[7])
        account_money = int(i[3])
    #buttons
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    btn_buy = objects.buttons.with_images(40, 390, 180,120,"images/buy_1.png", "images/buy_2.png")
    btn_sell = objects.buttons.with_images(300, 390, 180,120,"images/sell_1.png", "images/sell_2.png")
    #fonts, there are two different ones, one is for the speech bubble and one is for the players money amount
    font = pygame.font.SysFont('Consolas', 30)
    font2 = pygame.font.SysFont('Consolas', 25)
    #merchant's speech
    text = "Hey! Welcome \nto my shop!" 
    small_text = ""
    #images, the whole scene is just one image, because nothing was really meant to move so I thought it was easier
    merchant = objects.images.still(0,0,500,500,"images/merchant.png")
    bubble = objects.images.still(-30,-10,360,180,"images/bubbly.png")
    #displays player money
    money_display = f"{account_money}"
    
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
        merchant.draw(window)#draws the scene
        #gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT) #grid
        
        #buttons get drawn
        btn_exit.draw(window)
        btn_back.draw(window)
        btn_buy.draw(window)
        btn_sell.draw(window)
        bubble.draw(window)
        #text gets drawn
        objects.text.blit_text(window,text,(30,30,),font)
        objects.text.blit_text(window,small_text,(30,30,),font)
        objects.text.blit_text(window,money_display,(340,350,),font2)
    while run == True:
        display()
        
        for event in pygame.event.get():
            
            display()
            
            if btn_exit.update(pygame.mouse.get_pos(),event):#exits
                run = False
                pygame.quit()
                sys.exit()
            
            if btn_back.update(pygame.mouse.get_pos(),event):#previous page
                run = False
                manager.level = 4
            if btn_buy.update(pygame.mouse.get_pos(),event):#takes player to the buy page where they can upgrade their gear
                run = False
                manager.level = 6
            if btn_sell.update(pygame.mouse.get_pos(),event):#sells items
                #essentially how selling works, it takes whatever value was in inventory (treasure gets inputted as it's value) and adds it to money, then displays new money
                if account_inventory > 0:
                    money_add = account_money + account_inventory
                    money_display = f"{money_add}"
                    new_inventory = 0
                    objects.data_stuff.update_db(connection,"player_account",[f"money='{money_add}'",f"inventory='{new_inventory}'"],f"id={int(account_id)}")#updates account
                    text = "Have a \ngood day!"
                elif account_inventory <= 0:
                    text = ""
                    small_text = "Erm, You've got\nnothing to sell"
                    pass
                
                #print(f"Here|{result}")
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw