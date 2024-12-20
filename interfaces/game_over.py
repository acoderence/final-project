import pygame, sys, manager
import objects.buttons
import objects.images

oxygen=50
enemyhealth=50



def output(window): 
    bg=objects.images.animated(0,0,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/gameover.gif",40)
    text= objects.images.animated(250,300,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT,"images/youdrowned.gif",40)
    btn_exit= objects.buttons.with_images(450, 10, 40,40,"images/exit.png", "images/exit(2).png")
    btn_retry=objects.buttons.with_images(150, 350, 40,40,"images/retry.png", "images/retry(2).png")
    run = True



    while run:
        window.fill((255,255,255)) 
        btn_exit.draw(window)
        bg.draw(window)
        bg.update() 
        text.draw(window)
        text.update()
        btn_retry.draw(window)
       
       #if tank is empty, player dies and switches to gameover screen and says you drowned
       
    #if the player is killed by a fish then  it'll switch to gameover screen and says the fishes are biting...   
    if oxygen<=0:
             manager.level=7
             run=False
       
       
       
       
    for  event in pygame.event.get():
               
               

            # if user  QUIT then the screen will close
               if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                  #download pip install
    pygame.display.update() #update the display
    manager.fpsClock.tick(manager.fps) #speed of redraw e
            