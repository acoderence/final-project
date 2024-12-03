#Abbigail Spence and Brianna Wright
#November 25, 2024
# Deep Sea Diver Game 


import interfaces.game
import interfaces.intro
import pygame, sys, manager, interfaces.title, interfaces.help, interfaces.credits, interfaces.merchant, interfaces.intro, interfaces.buy
pygame.init()



window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Deep Sea Divers")


while True:
  if manager.level == 0:
    interfaces.title.output(window)
  elif manager.level == 1:
    interfaces.help.output(window)
  elif manager.level == 2:
    interfaces.credits.output(window)
  elif manager.level == 3:
    interfaces.game.output(window)
  elif manager.level == 4:
    interfaces.intro.output(window)
  elif manager.level == 5:
    interfaces.merchant.output(window)
  elif manager.level == 6:
    interfaces.buy.output(window)
    

  
    
