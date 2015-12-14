import pygame
from pygame.locals import *
pygame.init()

def how_to_play():
    pass

screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size, NOFRAME)

center = (screen_size[0]/2, screen_size[1]/2)

font = pygame.font.SysFont('Terminal', 32)
strings = ['Start', 'How to play', 'Copyright Nicks Games']
rendered_strings = []
for i in strings:
    rendered_strings.append(font.render(i, True, (210,105,30)))
    
boxes = []
for i in rendered_strings:
    boxes.append(i.get_rect())
    
boxes[0].center = center
boxes[1].center = (center[0], center[1]+40)
boxes[2].center = (center[0], screen_size[1]-30)

screen.fill((0,0,0))
done = False
while done==False:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            
        if event.type == MOUSEBUTTONDOWN:
            if boxes[0].collidepoint(pygame.mouse.get_pos()):
                import main
                
            elif boxes[1].collidepoint(pygame.mouse.get_pos()):
                how_to_play()
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]:
        quit()
        
    for i in range(len(strings)):
        screen.blit(rendered_strings[i], boxes[i])
        
        
    pygame.display.update()