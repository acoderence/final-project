import pygame, sys, manager
import objects.images
import objects.movable
import objects.enemy 
import objects.buttons
import objects.enemy 
import objects.data_stuff
import objects.diver
import objects.scissors
import objects.treasure
#lists
treasures=[]
inventory=[] 
attack=[]
bubble=[]
scissors=[]


def output(window): 
    global enemy_health
    font = pygame.font.SysFont('Consoles',35)  
    #connects to database
    connection = objects.data_stuff.create_connection('player_account.db')
    #connects to account that's logged in
    result = objects.data_stuff.select_db(connection,"player_account",[f"username ='{manager.account_user}'",f"password='{manager.account_pass}'"]).fetchall() 
    #accesses necessary values, like equiptment levels and inventory and give it a variable
    for i in result:
        bag_level = int(i[4])
        tank_level = int(i[5])
        weapon_level = int(i[6])
        account_id = int(i[0])
        account_inventory = int(i[7])
    print(result)#############################################################################################################delete later, just to make sure invenotry is returning to 0
    #max capacity for bag to carry, increases by bag level
    max = 0+(int(bag_level) * 5 )
   
    enemy_health = 80#enemy max health
    enemy_damage = 8 * weapon_level#damage enemy takes from player, increases as weapon gets upgraded
    
    warn = ""#string that displays warning when bag is full, it is blank for now so that it doesn't display it all the time
    
    mathy = int(account_inventory)/85 #Treausre gets added by value, and for ease we have each value the same, which  is 45. This checks how much treasure the player has collected by dividing by value
    if int(account_inventory) == 0:
        mathy = 0
    invent_make = mathy #invent make will be used later to add already existing treasure into the bag in case the player leaves the water before bag is full, they can come back and 
    #finsish filling from value they left off on
    
    ox_time = 0#trying to make the count down a little slower
    oxygen_count = 40 +(int(tank_level) * 15)#oxygen count increases with tank level
    en_run =0# same  concept of the ox_time but for enemy attack health countdown.
    
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/underwater.png")  #images in objects 
    #walls below are needed as borders for enemies to bounce off of
    wall = []
    wall.append(objects.images.still(0,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    wall.append(objects.images.still(500,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    top_wall = objects.images.still(0,-20,500,20,"images/wall.png")
    diver=objects.diver.move(0,0,100,100,"images/diver.gif",1,5)
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    treasures.append(objects.treasure.gems(230, 30,50,50,"images/yellowclam.png",2))
    treasures.append(objects.treasure.gems(120,130,50,50,"images/redgem.png",2))
    treasures.append(objects.treasure.gems(400,130,50,50,"images/purplegem.png",2))
    treasures.append(objects.treasure.gems(200,300,50,50,"images/pinkclam.png",2))
    treasures.append(objects.treasure.gems(70,250,50,50,"images/necklaceone.png",2))
    treasures.append(objects.treasure.gems(350,230,50,50,"images/magiclam.png",2))
    treasures.append(objects.treasure.gems(430,300,50,50,"images/pearls.png",2))
    treasures.append(objects.treasure.gems(310,400,50,50,"images/emerald.png",2))
    treasures.append(objects.treasure.gems(430,430,50,50,"images/diamond.png",2))
    treasures.append(objects.treasure.gems(50,410,50,50,"images/gem(1).png",2))
    seaweed=objects.images.animated(40,400,60,60,"images/kelp(2).gif",60)
    seaweedtwo=objects.images.animated(440,400,60,60,"images/kelp(2).gif",60)
    seaweedthree=objects.images.animated(300,450,60,60,"images/kelp(2).gif",60)
    seasnake=objects.images.animated(400,430,70,70,"images/sea snake.gif",60)
    crab=objects.images.animated(100,440,60,60,"images/small crab.gif",60)
   
   
    
    run = True
    pygame.display.set_caption("GAME")
    
    enemies = []#enemy generation
    x= 0
    for y in range (2):
            enemies.append(objects.enemy.moving(70 +(x*100),150+(y*150),100,100,"images/fish_1.png",5, enemy_health, enemy_damage))#damage increases as weapon upgrades
            x+=1     
               
        
    attack_count=0
  
      
    

    while run:
        bar = objects.movable.movable(diver.rect.x +20, diver.rect.y+90,oxygen_count, 10, "images/wall.png",1)#health bar. follows player and decreases in size as game goes on
        attack_count+=1
        window.fill((255,255,255))
        bg.draw(window)
        
        bar.draw(window)
 
        btn_back.draw(window)
        btn_exit.draw(window)
        seasnake.draw(window)
        seasnake.update()
        crab.draw(window)
        crab.update()
        seaweedthree.draw(window)
        seaweedthree.update()
        top_wall.draw(window)
        
        for bubbles in bubble: 
          bubbles.draw(window)
        for scissor in scissors:
            scissor.draw(window)
            
      
            
        
        seaweedtwo.draw(window)
        seaweedtwo.update()
        #below code is trying to make the timer slow down a little. It uses two timers, once increases by the seconds, while one only decreases when the other hits a certain value. The one that increases gets reset once that value is reached
        ox_time = ox_time +1
        if ox_time == 65:
            if oxygen_count >=2:#this also makes sure that bar can never be negative sizing
                ox_time = 0
                oxygen_count = oxygen_count -1
    
    ##redoo!!
        if oxygen_count<=2:#changes screen if oxygen runs out (player dies)
            manager.level=7
            run=False
       
        key_input = pygame.key.get_pressed()
       #scissors being thrown by the diver...attacks enemy for sure but cuts seaweed maybe
        if key_input[pygame.K_SPACE] and attack_count>50:
            scissors.append(objects.diver.move(diver.rect.x ,diver.rect.y , 30, 30,"images/scissors.png",20,2))
            attack_count=0   
            # update it
            
            
                 #remove scissor
        if len(scissors)>0:
            for scissor in scissors:
               scissor.rect.y +=2
               if scissor.rect.x >500:
                  scissors.remove(scissor)


   
        
        
        for scissor in scissors: #to kill enemy
             for x in enemies:#I'm hoping to give the enemies some lives, just so that they're more challenging, but I'm not sure how to make that work yet
                if pygame.sprite.collide_mask(scissor, x): 
                    scissors.remove(scissor)
                    x.hurt()
                    if x.health <=1:
                        enemies.remove(x)
        
        #code below is what makes sure that the player in-gmae inventory keeps the value the player had before they returned if they left with it partly filled.           
        if mathy<= 0:#it goes through that variable made and adds each value into the bag until it's at 0. If the player had nothing in it previously, than nothing happens
            mathy = 0
        elif mathy >= 1:
            invent_make = invent_make -1#subtract
            inventory.append(int(85)) 

        in_len = len(inventory)-1#I have to keep adding -1 to things becuase they always start at 0(they count 0 as 1 or soemthing), and then the numbers are never right 
        #if in_len <= -1:#so it doesn't show a negative number hopefully
            #in_len = 0
        bag_display = f"{in_len}/{max}"#displays the bag inventory out of the max that the player can collect, which increases with the bag level
        if in_len >= int(max): #If the bag is at mazimum capaxity, the invenotry fraction displays that the bag is full
            bag_display=f"{max}/{max}"
        #draws the inventory fraction and the warning of capacity    
        objects.text.blit_text(window,bag_display,(10,10),font)
        objects.text.blit_text(window,warn,(90,10),font)


        diver.draw(window)
        diver.movement()
        diver.update()
        diver.borders()
        bar.key_press()
     
                
        
        #so that the diver can resurface to sell and buy items
        if pygame.sprite.collide_mask(top_wall,diver):
            run=False
            manager.level=4
            
         

          
        
            
        for x in enemies:#draws enemy and makes them move
            x.draw(window)
            x.swim()
            pygame.draw.rect(window, (0, 238, 0),(x.rect.x +20, x.rect.y+100, x.health, 10))  #i moved the bar down here, the enemy health bar, 
            for i in wall:#if they hit the wall they reverse
                if pygame.sprite.collide_mask(x, i):
                    x.speed = -x.speed
            if pygame.sprite.collide_mask(x, diver):#if they hit the diver, the player loses oxygen
                en_run= en_run +1
                if en_run == 30:#similar timers as the oxygen count becuase enmies also drained oxygen too fast origianlly
                    oxygen_count = oxygen_count -3
                    en_run = 0
        
        #diver.health(window, oxygen_count)
        seaweed.draw(window)
        seaweed.update()
        
        for treasure in treasures:
            treasure.draw(window)
            if pygame.sprite.collide_mask(diver, treasure):                         
                if mathy<= int(max):  #if iventory is less than the max of bag capacity, makes it so that you can't collect more than the bag can hold                      
                    if len(inventory) <= int(max):#append each treasuere as value into list
                        treasures.remove(treasure)#remove treasure off the screen   
                        inventory.append(int(85))  #45 being price of individual treasure 
                    elif len(inventory) > int(max):#bag will be full, player can no longer collect
                            warn = "Bag is full"
                else:
                    warn="Bag is full"#there's two that make sure this text pops up becuase It's picky about showing up sometimes so this just makes sure that it does. 
        sum_inventory= ""#sum inventory would be what get's added to the inventory section on account dtatabase
        
        for i in inventory: #creates the string that gets updated to database which will be the inventory. I also makes sure that if there is nothing, it will be added as zero
            quick_add = f"{sum_inventory}"
            if quick_add == "":
                quick_add = 0
            i+=int(quick_add)
            sum_inventory = f"{i}"
         
        
        if len(sum_inventory) >=1:#updating invenotry in the database
            objects.data_stuff.update_db(connection,"player_account",[f"inventory='{sum_inventory}'"],f"id={int(account_id)}")
            
        
        
        for event in pygame.event.get(): 
            
            if btn_back.update(pygame.mouse.get_pos(),event):
                manager.level=4
                run=False #should not run or continue
            if btn_exit.update(pygame.mouse.get_pos(),event):
                sys.exit()
            
            
            if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
        
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw