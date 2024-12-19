import pygame, sys, manager, objects.buttons, objects.text, objects.data_stuff,objects.images



def output(window): 
    
    run = True
    connection = objects.data_stuff.create_connection('player_account.db')
    result = objects.data_stuff.select_db(connection,"player_account",[f"username ='{manager.account_user}'",f"password='{manager.account_pass}'"]).fetchall() 
    for i in result:
        account_id = int(i[0])
        account_money = int(i[3])
        bag_level = int(i[4])
        tank_level = int(i[5])
        weapon_level = int(i[6])
        
    btn_exit = objects.buttons.with_images(430,10,80,80,"images/exit.png", "images/exit(2).png")
    btn_back = objects.buttons.with_images(370, 10, 80,80,"images/back.png", "images/back(2).png")
    money = f"{account_money}"
    font = pygame.font.SysFont('Consolas', 25)
    font2 = pygame.font.SysFont('Consolas', 40)
    ttl = objects.images.still(30,-20,180,160,"images/upgrades.png")
    tank_price = 50+(int(tank_level)*100)
    bag_price= 50+(int(bag_level)*100)
    weapon_price= 50+(int(weapon_level)*100)
    tank_display = f"${tank_price}"
    bag_display = f"${bag_price}"
    weapon_display = f"${weapon_price}"
    tank_show =f"{tank_level}/5"
    bag_show =f"{bag_level}/5"
    weapon_show =f"{weapon_level}/5"
    prices= "Price of \nUpgrade:"
    level = "Current Level:"
    your_money = "Your Money"
    btn_buy1 = objects.buttons.with_background(20, 160, 150,60, "Montserrat", 40, (245, 138, 66), (245, 78, 66),(252, 252, 252),(204, 196, 196)," Tank")
    btn_buy2 = objects.buttons.with_background(20, 260, 150,60, "Comfortaa", 40, (245, 138, 66), (245, 78, 66),(252, 252, 252),(204, 196, 196)," Bag")
    btn_buy3 = objects.buttons.with_background(20, 360, 150,60, "Comfortaa", 40, (245, 138, 66), (245, 78, 66),(252, 252, 252),(204, 196, 196)," Scissors")
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
        window.fill((217, 198, 167))#tan backround. feels very shop-like idk
        gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)#grid
        btn_exit.draw(window)
        btn_back.draw(window)
        btn_buy1.draw(window)
        btn_buy2.draw(window)
        btn_buy3.draw(window)
        #pplayers money gets diaplyed to see how much they have
        objects.text.blit_text(window,money,(200,460,),font)
        #prices title and your level tittle displayed (titled just so the player knows what they're looking at) also your money title
        objects.text.blit_text(window,prices,(190, 90,),font)
        objects.text.blit_text(window,level,(350, 90,),font)
        objects.text.blit_text(window,your_money,(20, 460,),font)
        #price of upgrade gets displayed
        objects.text.blit_text(window,tank_display,(190, 160,),font)
        objects.text.blit_text(window,bag_display,(190, 260,),font)
        objects.text.blit_text(window,weapon_display,(190, 360,),font)
        #shows current level of equiptment
        objects.text.blit_text(window,tank_show,(350, 160,),font)
        objects.text.blit_text(window,bag_show,(350, 260,),font)
        objects.text.blit_text(window,weapon_show,(350, 360,),font)
        ttl.draw(window)
        
    while run == True:
        display()
       
       
        for event in pygame.event.get(): 
            if btn_buy1.update(pygame.mouse.get_pos(),event):
                if tank_level < 10:
                    if account_money>tank_price:
                        account_money-=tank_price
                        tank_level += 1
                        objects.data_stuff.update_db(connection,"player_account",[f"money='{account_money}'",f"tank_level='{tank_level}'"],f"id={int(account_id)}")
                        money = f"{account_money}"
                        tank_price = 50+(int(tank_level)*100)
                        tank_display = f"${tank_price}"
                        tank_show =f"{tank_level}/5"
                        display()
                        print(result)
                        
            if btn_buy2.update(pygame.mouse.get_pos(),event):
                if bag_level < 5:
                    if account_money>bag_price:
                        account_money-=bag_price
                        bag_level += 1
                        objects.data_stuff.update_db(connection,"player_account",[f"money='{account_money}'",f"bag_level='{bag_level}'"],f"id={int(account_id)}")
                        money = f"{account_money}"
                        money = f"{account_money}"
                        bag_price = 50+(int(bag_level)*100)
                        bag_display = f"${bag_price}"
                        bag_show =f"{bag_level}/5"
                        display()
                        print(result)
                        
                
            
            if btn_buy3.update(pygame.mouse.get_pos(),event):
                if weapon_level < 5:
                    if account_money>weapon_price:
                        account_money-=weapon_price
                        weapon_level += 1
                        objects.data_stuff.update_db(connection,"player_account",[f"money='{account_money}'",f"weapon_level='{weapon_level}'"],f"id={int(account_id)}")
                        money = f"{account_money}"
                        money = f"{account_money}"
                        weapon_price = 50+(int(weapon_level)*100)
                        weapon_display = f"${weapon_price}"
                        weapon_show =f"{weapon_level}/5"
                        display()
                        print(result)
                        
                
                    
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