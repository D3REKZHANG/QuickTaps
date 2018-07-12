import pygame
from pygame.locals import *

pygame.font.init()

#Images

bg_list = [
	pygame.image.load('images/backgrounds/castle_sky_light_blue.jpg'),
	pygame.image.load('images/backgrounds/fantasy_asian_kingdom.jpg'),
	pygame.image.load('images/backgrounds/forest_house_fall.jpg'),
	pygame.image.load('images/backgrounds/future_space_water.jpg'),
	pygame.image.load('images/backgrounds/purple_clouds.jpg'),
	pygame.image.load('images/backgrounds/raining_cool_girl.jpg')
]
banner = pygame.image.load('images/banner.png')
icon = pygame.image.load('images/icon.ico')

#Variable Definitions
title = 'title'
menu = 'menu'
game = 'game'
endscreen = 'endscreen'
winscreen = 'winscreen'
paused = 'paused'

up = 'up'
down = 'down'
left = 'left'
right = 'right'

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (0, 190, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)

horizontal = "horizontal"
vertical = "vertical"

#FONTS
courier18 = pygame.font.SysFont('courier new', 18)
courier30 = pygame.font.SysFont('courier new', 30)
segoe30 = pygame.font.SysFont('segoe ui', 30)
segoe72 = pygame.font.SysFont('segoe ui', 72)
verdana18 = pygame.font.SysFont('verdana', 18)
impact72 = pygame.font.SysFont('impact', 72)

#Actual Settings xD
window_width = 450
window_height = 450

clock = pygame.time.Clock()
fps = 60
