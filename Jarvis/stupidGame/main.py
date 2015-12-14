import pygame
from pygame.locals import *
pygame.init()

from random import randint

from vector2 import Vector2 as vec2

w,h = screen_size = (640,480)
center = vec2(w/2,h/2)

screen = pygame.display.set_mode(screen_size)

enemyImg = pygame.image.load("GenericEnemy.png").convert()

class enemy(pygame.sprite.Sprite):

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.health = 100
		self.pos = vec2(*pos)
		self.image = enemyImg
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.speed = 1

	def update(self, tp, playerPos):
		normalizedDirection = vec2().from_points(self.pos, playerPos)
		self.pos+=normalizedDirection*self.speed*tp
		self.rect.center = self.pos

	def explode(self, playerPos, group):
		normalizedDirection = vec2().from_points(self.pos, playerPos)*-1

		def rO():
			return randint(-10,10)

		group.add(enemy(self.pos+normalizedDirection+vec2(rO(),rO())))
		group.add(enemy(self.pos+normalizedDirection+vec2(rO(),rO())))
		self.kill()

enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy((w/4,h/4)))

clock = pygame.time.Clock()

done = False
while not done:
	time_passed = clock.tick()
	time_passed_seconds = time_passed/1000.

	for event in pygame.event.get():
		if event.type == QUIT:
			done = True

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True

			if event.key == K_SPACE:
				for ENEMY in enemyGroup.sprites():
					ENEMY.explode(center, enemyGroup)

	for ENEMY in enemyGroup.sprites():
		ENEMY.update(time_passed_seconds, pygame.mouse.get_pos())
	#print len(enemyGroup.sprites())

	screen.fill((0,0,0))
	enemyGroup.draw(screen)

	pygame.display.update()
pygame.quit()
