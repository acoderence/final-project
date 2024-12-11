import pygame, sys, manager
import objects.images
import objects.movable
import objects.enemy 
import objects.buttons
import objects.enemy 

treasures=[]


def output(window): 
    enemy_health = 3
    font = pygame.font.SysFont('Consoles',35)  
    bg= objects.images.still(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/underwater.png")  #images in objects 
    wall = []
    wall.append(objects.images.still(0,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    wall.append(objects.images.still(500,0,20,manager.WINDOW_HEIGHT, "images/wall.png"))
    diver=objects.images.animated(0,0,100,100,"images/diver.gif",5)
    btn_back=objects.buttons.with_images(400, 10, 40,40,"images/back.png", "images/back(2).png")
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    treasures.append(objects.movable.movable(200, 220,50,50,"images/yellowclam.png",2))
    treasures.append(objects.movable.movable(100,100,50,50,"images/redgem.png",2))
    treasures.append(objects.movable.movable(10,40,50,50,"images/purplegem.png",2))
    treasures.append(objects.movable.movable(0,0,50,50,"images/pinkclam.png",2))
    treasures.append(objects.movable.movable(0,0,50,50,"images/necklaceone.png",2))
    treasures.append(objects.movable.movable(0,0,50,50,"images/magiclam.png",2))
    treasures.append(objects.movable.movable(0,0,50,50,"images/pearls.png",2))
    treasures.append(objects.movable.movable(150,300,50,50,"images/emerald.png",2))
    treasures.append(objects.movable.movable(90,60,50,50,"images/diamond.png",2))
    treasures.append(objects.movable.movable(250,100,50,50,"images/gem(1).png",2))
    seaweed= objects.images.animated(40,400,40,40,"images/kelp(2).gif",60)
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
        window.fill((255,255,255))
        bg.draw(window)
        btn_back.draw(window)
        btn_exit.draw(window)
        diver.draw(window)
        diver.update()
        seaweed.draw(window)
        seaweed.update()
        for treasure in treasures:
            treasure.draw(window)
        
        for x in enemies:
                x.draw(window)
                x.swim()
                for i in wall:
                    if pygame.sprite.collide_mask(x, i):
                        x.speed = -x.speed
                    
            
        
        
       
       
       
        for event in pygame.event.get(): 
           if btn_back.update(pygame.mouse.get_pos(),event):
                manager.level=0
                run=False #should not run or continue
           if btn_exit.update(pygame.mouse.get_pos(),event):
               sys.exit()
           
           
           if event.type == pygame.QUIT: #Quits
                            pygame.quit()
                            sys.exit()
              
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw