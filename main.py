import pygame
from pygame.locals import *
import random
import sys
from settings import *

pygame.font.init()
pygame.init()


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super(Pad, self).__init__()

        self.width, self.height = 95,95

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(black)
        self.image.set_alpha(160)

        self.rect = self.image.get_rect()

        self.pos_x,self.pos_y = [-1,-1]
        self.prev_pos = [-1,-1]

    def set_pos(self):
        global pad_pos
        self.prev_pos = [self.pos_x,self.pos_y]
        try:
            pad_pos.remove([self.pos_x,self.pos_y])
        except:
            pass

        self.pos_x = random.randint(0,3)
        self.pos_y = random.randint(0,3)

        if [self.pos_x,self.pos_y] in pad_pos or self.prev_pos == [self.pos_x,self.pos_y]:
            self.set_pos()
        else:
            pad_pos.append([self.pos_x,self.pos_y])

        self.rect.x = (self.pos_x*(self.width+5)) + 25
        self.rect.y = (self.pos_y*(self.height+5)) + 25

    def update(self):
        global ACTION_CLICK,ACTION_HOVER,score,GAME_MODE,CLICK,pad_pos

        if mouse_collide(self,self.mouse):
            self.image.set_alpha(210)
            if CLICK:
                score += 1
                self.set_pos()
        else:
            self.image.set_alpha(160)
        pygame.draw.rect(window,white,(self.rect.x-2,self.rect.y-2,self.width+4,self.height+4),2)


def text(text, font, size, color, x, y):
    font_style = str(font)
    font_size = size

    text_font = pygame.font.SysFont(font_style, font_size)

    message = text_font.render(text, True, color)

    window.blit(message, (x, y))

def mouse_collide(obj,mouse):
    if obj.rect.x + obj.height > mouse[0] > obj.rect.x \
    and obj.rect.y + obj.width > mouse[1] > obj.rect.y:
        return True
    else:
        return False

if (__name__ == "__main__"):

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Quick Taps")
    pygame.display.set_icon(icon)

    GAME_MODE = title

    active_object_list = pygame.sprite.Group()

    pad_pos = []

    pad1 = Pad()
    pad1.set_pos()
    pad2 = Pad()
    pad2.set_pos()

    active_object_list.add(pad1,pad2)

    ACTION_CLICK = None
    ACTION_HOVER = None
    CLICK = False

    score = 0
    winscore = 15
    starttime = False
    time = 0

    endscreen_alpha = 0
    winscreen_alpha = 255

    while 1:

        while (GAME_MODE == title):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    GAME_MODE = game
                    bg = bg_list[random.randint(0,len(bg_list)-1)]

            window.fill(black)

            text("Quick Taps",'segoe ui',60,white,90,180)

            clock.tick(60)
            time = 0
            score = 0
            starttime = False
            endscreen_alpha = 0
            winscreen_alpha = 255
            pygame.display.update()

        while (GAME_MODE == game):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if (event != None):
                    if (event.type == pygame.KEYDOWN):
                        GAME_MODE = paused
                        s = pygame.Surface((window_width,window_height))  
                        s.set_alpha(200)               
                        s.fill(black)          
                        window.blit(s, (0,0))    
                        text("PAUSED",'segoe ui',40,white,160,190)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        CLICK = True
                        starttime = True
                        if mouse_collide(pad1,pygame.mouse.get_pos()) == False \
                        and mouse_collide(pad2,pygame.mouse.get_pos()) == False:
                            GAME_MODE = endscreen

            if GAME_MODE == paused:
                break

            pad1.mouse,pad2.mouse = pygame.mouse.get_pos(),pygame.mouse.get_pos()

            active_object_list.update()

            screen_fade = pygame.Surface((window_width,window_height));screen_fade.set_alpha(60);screen_fade.fill(white)

            window.blit( bg, (0,0))
            window.blit( screen_fade, (0,0) )
            active_object_list.draw(window)

            CLICK = False

            if score == winscore:
                GAME_MODE  = winscreen

            if starttime:
                time += 1

            clock.tick(fps)
            pygame.display.update()

        while (GAME_MODE == paused):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    GAME_MODE = game

            clock.tick(fps)
            pygame.display.update()

        while (GAME_MODE == endscreen):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    GAME_MODE = title

            window.blit(bg,(0,0))
            s = pygame.Surface((window_width,window_height))
            if endscreen_alpha < 180:
                endscreen_alpha += 5
            s.set_alpha(endscreen_alpha)
            s.fill((180,0,0))

            window.blit(s,(0,0))

            clock.tick(fps)
            pygame.display.update()

        while (GAME_MODE == winscreen):

            endtime = str(int(time/60))+":"+str(int(time/6))
            message = segoe72.render(endtime, True,black)

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    GAME_MODE = title

            window.blit(bg,(0,0))
            s = pygame.Surface((window_width,window_height))
            if winscreen_alpha > 0:
                winscreen_alpha -= 5
            s.set_alpha(winscreen_alpha)
            s.fill((255,255,255))
            window.blit(s,(0,0))
            window.blit(banner,(0,0))
            window.blit(message,(window_width/2 - segoe72.size(endtime)[0]/2,175) )

            clock.tick(fps)
            pygame.display.update()






































