import pygame, sys, manager, objects.images, objects.buttons, sqlite3, objects.data_stuff, objects.text, objects.search


def output(window): 
    title_text = objects.images.still(20,20,450,150,"images/welcome.png")
    message = ""
    font = pygame.font.SysFont('Consolas', 20)
    run = True
    btn_play = objects.buttons.with_images(150,310, 250, 150, "images/play_1.png", "images/play_2.png")
    btn_exit = objects.buttons.with_images(420,10, 100, 50, "images/exit.png", "images/exit(2).png")
    btn_help = objects.buttons.with_images(300,400, 150, 100, "images/help_1.png", "images/help_2.png")
    btn_credit = objects.buttons.with_images(100,400, 150, 100, "images/credits_1.png", "images/credits_2.png")
    btn_new = objects.buttons.with_images(330,350, 100, 50, "images/New_1.png", "images/New_2.png")
    
    txt_user = objects.text.input(170,170, 150,50,'Consolas',20,(0,0,0), (61, 132, 209))
    txt_pass = objects.text.input(170,250, 150,50,'Consolas',20,(0,0,0), (61, 132, 209))
    
    connection = objects.data_stuff.create_connection('player_account.db')
    
    if connection is not None: #checks that there is a connection
        objects.data_stuff.create_table(connection,"player_account",["username TEXT","password TEXT", "money TEXT", "bag_level TEXT", "tank_level TEXT", "weapon_level TEXT", "inventory TEXT"])#createsthe table if there is a connection
    else: #error checking
        print("Error! cannot create the database connection.")
        
    def display():
        window.fill((94, 188, 224))#blue background to look like water hopefully
        gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)#grid
        
        title_text.draw(window)
        btn_play.draw(window)
        btn_exit.draw(window)
        btn_help.draw(window)
        btn_credit.draw(window)
        btn_new.draw(window)
        
        txt_user.draw(window)
        txt_pass.draw(window)
        
        objects.text.blit_text(window,message,(80, 310),font)
        
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

    while run == True:
        display()
       
       
        for event in pygame.event.get(): 
            
            txt_user.update(pygame.mouse.get_pos(),event) 
            txt_pass.update(pygame.mouse.get_pos(),event) 
            user_text = txt_user.text.lower()
            pass_text = txt_pass.text.lower()
          
            if btn_play.update(pygame.mouse.get_pos(),event):
                string = ""
                check = ""
                result = objects.data_stuff.select_db(connection,"player_account",[f"username ='{str(user_text)}'",f"password='{str(pass_text)}'"]).fetchall() 
                for i in result:
                    words = f"\n{i}"
                    comma =" , "#this separates each number so that it looks cleaner
                    string += comma#adds commas
                    string += str(words)#adds each total
                    check = string[3:]#this removes the fist comma and its spaces because we don't need one at the beginning before the first value 
                #checks that string is working
                
                
                if user_text == "":
                    message = "please fill out this field"
                elif pass_text == "":
                    message = "please fill out this field"
                else:
                    if len(check) <= 0:
                        message = "username or password is incorrect"
                    elif len(check) >= 1:
                        run = False
                        manager.account_user =f"{user_text}"
                        manager.account_pass = f"{pass_text}"
                        manager.level = 4
            if btn_help.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 1
            if btn_credit.update(pygame.mouse.get_pos(),event):
                run = False
                manager.level = 2
            
            if btn_new.update(pygame.mouse.get_pos(),event): 
                checker = False
                
                
                result = objects.data_stuff.select_db(connection,"player_account",[f"username ='{str(user_text)}'",f"password='{str(pass_text)}'"]).fetchall()
                
                if len(result) > 0:
                    checker = True
                
                if user_text == "":
                    message = "please fill out this field"
                elif pass_text == "":
                    message = "please fill out this field"
                elif len(user_text) < 4:
                    message = "Username must have 4 or more characters"
                elif len(pass_text) < 4:
                    message = "please mmust have 4 or more characters"
                elif checker == True:
                    message = "That account already exists"
                elif checker ==  False:
                    objects.data_stuff.insert_db(connection,"player_account",["username","password", "money","bag_level","tank_level", "weapon_level", "inventory"],[f"{user_text}",f"{pass_text}","0","1","1","1","0"])
                    message = "new account made"
            if btn_exit.update(pygame.mouse.get_pos(),event):
                run = False
                
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw