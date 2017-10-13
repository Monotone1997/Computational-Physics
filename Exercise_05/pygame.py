background_image_filename = 'bg.jpg'
sprite_image_filename = 'cannon.jpg'

import pygame
from pygame.locals import *
from sys import exit
from math import *

g=25000

pygame.init()

screen = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

x, y = 0., 320.
speed_x, speed_y = 50., -150.

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background, (0, 0))
	screen.blit(sprite, (x, y))

	time_passed = clock.tick(100)
	time_passed_seconds = time_passed / 1000.0

	x += speed_x * time_passed_seconds
	y += speed_y * time_passed_seconds + (0.5*g*time_passed_seconds**2)

	pygame.display.update()