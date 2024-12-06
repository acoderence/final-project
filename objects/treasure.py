import sqlite3,pygame,sys
import objects.images
import objects.movable
import objects.buttons
import manager
import objects.bag as bag


treasure=[]


def output(window):
    treasure.append(objects.movable.movable(30,200,150,150,"images/gem(1).png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/emerald.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/diamond.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/magiclam.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/pinkclam.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/pearls.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/necklaceone.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/purplegem.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/redgem.png",2))
    treasure.append(objects.movable.movable(30,200,150,150,"images/yellowclam.png",2))
    
    btn_collect= objects.buttons.with_images(450, 10, 40,40,"images/collect(1).png", "images/collect(2).png") ###look over


    def display():
        btn_collect.draw(window)


#I'm not sure if this will work but hopefully if a treasure is collected, it will add a value to the bag inventory so we can add it up later. this system
#makes it so that all treasure has the same value but if we can get it working then we can adjust that later. 
def collect(diver,treasure):

    if pygame.sprite.collide_mask(diver, treasure):
        bag.inventory.append(int(80))
