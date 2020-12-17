
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

#Images

bg_list = [
	pygame.image.load('images/backgrounds/castle_sky_light_blue.jpg'),
	pygame.image.load('images/backgrounds/april.jpg'),
	pygame.image.load('images/backgrounds/your_name.jpg'),
	pygame.image.load('images/backgrounds/forest_house_fall.jpg'),
	pygame.image.load('images/centre.png'),
	pygame.image.load('images/backgrounds/raining_cool_girl.jpg'),
	pygame.image.load('images/backgrounds/purple_mountain_trees.jpg'),
	pygame.image.load('images/backgrounds/fantasy_asian_kingdom.jpg'),
	pygame.image.load('images/backgrounds/future_space_water.jpg'),
]
banner = pygame.image.load('images/banner.png')
help_bg = pygame.image.load('images/help_bg.png')

#Variable Definitions
title = 'title'
menu = 'menu'
help_screen = 'help_screen'
game = 'game'
arcade = 'arcade'
endscreen = 'endscreen'
winscreen = 'winscreen'
paused = 'paused'
bg_select = 'bg_select'

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
ps = 60
