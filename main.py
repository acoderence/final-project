#Abbigail Spence and Brianna Wright
#November 25, 2024
# Deep Sea Diver Game 


import interfaces.game
import pygame, sys, manager, interfaces.title, interfaces.help, interfaces.credits
pygame.init()



window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Deep sea Divers")


while True:
  if manager.level == 0:
    interfaces.title.output(window)
  elif manager.level == 1:
    interfaces.help.output(window)
  elif manager.level == 2:
    interfaces.credits.output(window)
  elif manager.level == 3:
    interfaces.game.output(window)
    
