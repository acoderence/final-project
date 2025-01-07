import pygame

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
level = 0

#these here below keep track of who is logged into the game. I pretty much just needed a way to know what username and password was inputted into the sign in
#So that I could access it later on, for updates, inventory, etc. 
account_user =""
account_pass =""