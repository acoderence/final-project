import pygame
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    #From https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
class input(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height, font_name,font_size,text_color,back_color,starting_text="",max_length=20):
        super().__init__()
        self.image = pygame.Surface([width+4, height+4],pygame.SRCALPHA).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.writing = pygame.Surface([width, height],pygame.SRCALPHA).convert_alpha()
       
        self.font_used = pygame.font.SysFont(font_name, font_size)
       
        self.back_color=back_color
        self.text_color = text_color
        self.text=starting_text
        self.max_length = max_length
   
       
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
        self.is_active = False

        self.write()
    def write(self):
       
        self.text_surface = self.font_used.render(self.text, True, self.text_color)      
        self.image.fill((0,0,0))
        self.writing.fill(self.back_color)  
        self.writing.blit(self.text_surface,(0,0))
        self.image.blit(self.writing, (2, 2))
       
    def update(self,pos,event):                    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is within the text input rect
            self.is_active = self.rect.collidepoint(pos)
        elif event.type == pygame.KEYDOWN and self.is_active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                #print("Entered text:", self.text)  # You can modify this to handle the entered text
                self.text = ""
            elif len(self.text) < self.max_length:
                self.text += event.unicode
        self.write()
    def draw(self, screen):
        # Render the text surface
       screen.blit(self.image,self.rect)