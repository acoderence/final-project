import pygame, sys 
    
import pygame,sys
import objects.enemy
import objects.images
import manager
import objects.movable

class air(objects.images.still): ##check
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height, image_to_use)
        self.speed = speed
    


pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 10
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)                

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)
    window.blit(text, text_rect)
    pygame.display.flip()