#Abbigail Spence and Brianna Wright
#November 25, 2024
# Deep Sea Diver Game 


import pygame, sys, manager, interfaces.title
pygame.init()



window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Deep sea Divers")

if manager.level == 0:
    interfaces.title.output(window)
