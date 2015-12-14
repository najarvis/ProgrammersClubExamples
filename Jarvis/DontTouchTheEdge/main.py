import pygame

from pygame.locals import *

from math import cos
import glob
import random
pygame.init()

screen_size = (798,400)

screen = pygame.display.set_mode(screen_size)

ps = glob.glob("*.mp3")
random.shuffle(ps)
#song = ps[0]
song = 'Hypnotica.mp3'

pygame.mixer.music.load(song)


class Ball(object):

    def __init__(self, map1, pos=(20,20)):
        self.x, self.y =  pos
        #self.image = get_image(1,1,1,0,map1)
        self.image = map1


def lerp(c1, c2, a):
    return c1+(c2-c1)*a

# def lerp(a, b, x):
#     ft = x*3.1415927
#     f=(1-cos(ft))*.5
#     
#     return a*(1-f)+b*f



#ball_image = pygame.image.load("Balls.bmp").convert()
size = 24
ball_image = pygame.Surface((size,size))
ball_image.fill((128,0,128))
for i in range(size/4):
    pygame.draw.circle(ball_image, (lerp(0,200,i/(size/4.)), lerp(0,200,i/(size/4.)), lerp(0,200,i/(size/4.))), (size/2,size/2), size/2-i*2)
ball_image.set_colorkey((128,0,128))

map_image = pygame.Surface(screen_size)

center = (screen_size[0]/2, screen_size[1]/2)


high_score = 0.

for i in range(200):
    pygame.draw.line(map_image, (0, lerp(255,0,i/200.), lerp(0,255,i/200.)), (screen_size[0]/2+i, 0), (screen_size[0]/2+i, screen_size[1]))
    pygame.draw.line(map_image, (0, lerp(255,0,i/200.), lerp(0,255,i/200.)), (screen_size[0]/2-i, 0), (screen_size[0]/2-i, screen_size[1]))

for i in range(200):
    pygame.draw.line(map_image, (lerp(255,0,i/200.), 0, lerp(0,255,i/200.)), (i,0), (i,screen_size[1]))
    pygame.draw.line(map_image, (lerp(255,0,i/200.), 0, lerp(0,255,i/200.)), (screen_size[0]-i,0), (screen_size[0]-i,screen_size[1]))

font = pygame.font.SysFont(None, 50)
game_over = "Game Over!"
game_over_rendered=font.render(game_over, True, (255,255,255))
game_over_box = game_over_rendered.get_rect()
game_over_box.center = center

small_font = pygame.font.SysFont(None, 25)
reset = 'Press R to restart'
reset_rendered = small_font.render(reset, True, (255,255,255))
reset_box = reset_rendered.get_rect()
reset_box.center = (center[0], center[1]+20)
ball = Ball(ball_image, center)
w,h = ball.image.get_size()
ball.x = center[0]-w/2
ball.y = center[1]-h/2

pygame.display.set_caption("Don't Touch The Edge!!!")

pygame.image.save(map_image, "Map_updated.bmp")

acceleration=10.

clock = pygame.time.Clock()

direction = 'Xr'

score = 0.0

pygame.mixer.music.play(-1)

last_pos = [center[0]-w/2, center[1]-h/2]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    time_passed = clock.tick(60)
    time_passed_seconds = time_passed/1000.

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        if direction!='Xr':
            direction = 'Xl'

    if pressed_keys[K_RIGHT]:
        if direction!='Xl':
            direction = 'Xr'

    if pressed_keys[K_UP]:
        if direction!='Yd':
            direction = 'Yu'

    if pressed_keys[K_DOWN]:
        if direction!='Yu':
            direction = 'Yd'

    screen.blit(map_image, (0,0))
    screen.blit(ball.image, (ball.x, ball.y))

    if ball.y<0 or ball.y>screen_size[1]-ball.image.get_height() or ball.x<0  or ball.x>screen_size[0]-ball.image.get_height():
        screen.blit(game_over_rendered, game_over_box)
        screen.blit(reset_rendered, reset_box)
        acceleration = 0
        if pressed_keys[K_r]:
            acceleration = 1
            ball.x = center[0]-w/2
            ball.y = center[1]-h/2
            score = 0
            direction = 'Xr'
            last_pos = [center[0]-w/2, center[1]-h/2]
            for i in range(200):
                pygame.draw.line(map_image, (0, lerp(255,0,i/200.), lerp(0,255,i/200.)), (screen_size[0]/2+i, 0), (screen_size[0]/2+i, screen_size[1]))
                pygame.draw.line(map_image, (0, lerp(255,0,i/200.), lerp(0,255,i/200.)), (screen_size[0]/2-i, 0), (screen_size[0]/2-i, screen_size[1]))

            for i in range(200):
                pygame.draw.line(map_image, (lerp(255,0,i/200.), 0, lerp(0,255,i/200.)), (i,0), (i,screen_size[1]))
                pygame.draw.line(map_image, (lerp(255,0,i/200.), 0, lerp(0,255,i/200.)), (screen_size[0]-i,0), (screen_size[0]-i,screen_size[1]))


            #pygame.mixer.music.play(-1)

    else:
        acceleration+=time_passed_seconds*100
        score += time_passed_seconds

    if direction == 'Yu':
        ball.y-=time_passed_seconds*acceleration
    elif direction == 'Yd':
        ball.y+=time_passed_seconds*acceleration

    if direction == 'Xl':
        ball.x-=time_passed_seconds*acceleration
    elif direction == 'Xr':
        ball.x+=time_passed_seconds*acceleration
        
    pygame.draw.line(map_image, (255,255,255), last_pos, (ball.x+w/2, ball.y+w/2), 2)
    last_pos = [ball.x+w/2, ball.y+w/2]

    score_render = font.render("%.3f"%score, True, (255,255,255))
    screen.blit(score_render, (0,0))

    high_score_render = font.render("High Score: %.3f"%high_score, True, (255,255,255))
    high_score_box = high_score_render.get_rect()
    high_score_box.center = (center[0], 20)
    screen.blit(high_score_render, high_score_box)

    high_score = max(high_score, score)

    pygame.display.flip()

