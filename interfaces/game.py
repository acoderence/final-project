import pygame, sys, manager
import objects.images
import objects.movable
import objects.enemy 
import objects.buttons
import objects.enemy 
import objects.bag
import objects.data_stuff
import objects.txt_files
treasures=[]

inventory = []

def output(window): 
    enemy_health = 3
    connection = objects.data_stuff.create_connection('u_account.db')
    result = objects.data_stuff.select_db(connection,"account",[f"username ='test'",f"password='test'"]).fetchall() 
    print(result)
    for i in result:
        bag_level = int(i[4])
        tank_level = int(i[5])
        weapon_level = int(i[6])
    
    max = 5+(int(bag_level) * 5 )
    print(bag_level, tank_level, weapon_level)
    font = pygame.font.SysFont('Consoles',35)  
    bag_display = "0/10"
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/underwater.png")  #images in objects 
    wall = []
    wall.append(objects.images.still(0,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    wall.append(objects.images.still(500,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    diver=objects.movable.movable(0,0,100,100,"images/diver.gif",5)
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    treasures.append(objects.movable.movable(200, 220,50,50,"images/yellowclam.png",2))
    treasures.append(objects.movable.movable(100,100,50,50,"images/redgem.png",2))
    treasures.append(objects.movable.movable(10,40,50,50,"images/purplegem.png",2))
    treasures.append(objects.movable.movable(200,300,50,50,"images/pinkclam.png",2))
    treasures.append(objects.movable.movable(75,70,50,50,"images/necklaceone.png",2))
    treasures.append(objects.movable.movable(145,40,50,50,"images/magiclam.png",2))
    treasures.append(objects.movable.movable(100,400,50,50,"images/pearls.png",2))
    treasures.append(objects.movable.movable(150,300,50,50,"images/emerald.png",2))
    treasures.append(objects.movable.movable(90,60,50,50,"images/diamond.png",2))
    treasures.append(objects.movable.movable(250,100,50,50,"images/gem(1).png",2))
    seaweed=objects.images.animated(40,400,60,60,"images/kelp(2).gif",60)
    seaweedtwo=objects.images.animated(440,400,60,60,"images/kelp(2).gif",60)
    btn_collect= objects.buttons.with_images(450, 10, 40,40,"images/collect(1).png", "images/collect(2).png") ###look over
    #scissors= objects.images.still()
    
    
    run = True
    pygame.display.set_caption("GAME")
    
    enemies = [] #look at this agin later cuase I'm not too sure how well that is, I think for math for enemy location
        # could totally copy from the 2d list program
    x=0
    for y in range (2):
            enemies.append(objects.enemy.moving(70 +(x*100),150+(y*150),100,100,"images/fish_1.png",5))
            x+=1
            
             
        
    



    while run:
        
        diver.key_press()
        window.fill((255,255,255))
        bg.draw(window)
        btn_back.draw(window)
        btn_exit.draw(window)
        btn_collect.draw(window)
        seaweedtwo.draw(window)
        seaweedtwo.update()
        
        
        diver.draw(window)
         
        #diver.update() #I didn't know how to make movement work so I just changed it to objects.movable.movable so that he could move so he could collect treasure so I could test the bag. We can fix it later.
        seaweed.draw(window)
        seaweed.update()
        for treasure in treasures:
            treasure.draw(window)
            for treasure in treasures:
                if pygame.sprite.collide_mask(diver, treasure):
                    treasures.remove(treasure)#remove treasure off the screen
                    inventory.append(85)#append each treasuere as value into list
                    if len(inventory) < int(max):
                        inventory.append  (treasure)   
                    elif len(inventory) >= int(max):
                            warn = "Bag is full"
            
       
            
        for x in enemies:
                x.draw(window)
                x.swim()
                for i in wall:
                    if pygame.sprite.collide_mask(x, i):
                        x.speed = -x.speed
                    
            
        
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