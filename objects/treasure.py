import sqlite3,pygame,sys
import objects.images
import objects.movable
import objects.buttons
import manager


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

      








    
    

     