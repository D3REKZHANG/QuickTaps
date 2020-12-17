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
        global ACTION_CLICK,ACTION_HOVER,score,GAME_STATE,CLICK,pad_pos

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

def button(x,y,w,h,a_hover,a_click):

    global window,ACTION_HOVER,ACTION_CLICK,CLICK

    mouse = pygame.mouse.get_pos()                 #Get Mouse Position

    if x+w > mouse[0] and mouse[0] > x and y+h > mouse[1] and mouse[1] > y:  #If mouse position is inside the box
        #pygame.draw.rect( window, (255,255,255), (x,y,w,h) )
        ACTION_HOVER = a_hover
        if CLICK:
            ACTION_CLICK = a_click                 #If clicked, set click action
    elif ACTION_HOVER == a_hover:
        ACTION_HOVER = None
    if ACTION_CLICK == a_click and not CLICK:
        ACTION_CLICK = None

def reset():
    global time, score, starttime, CLICK, ACTION_CLICK, ACTION_HOVER
    time = 0
    score = 0
    starttime = False
    CLICK = False
    ACTION_CLICK = None
    ACTION_HOVER = None
    pad1.set_pos()
    pad2.set_pos()
    pad3.set_pos()

def menu_anim():
    for y in range(180,120,-5):
        window.fill(black)
        text("Quick Taps",'segoe ui',60,white,90,y)
        clock.tick(60)
        pygame.display.update()

    for x in range(-200,188,40):
        window.fill(black)
        text("Quick Taps",'segoe ui',60,white,90,120)
        text("Play",'segoe ui',40,white,x,220)
        clock.tick(60)
        pygame.display.update()

    for x in range(-200,158,40):
        window.fill(black)
        text("Quick Taps",'segoe ui',60,white,90,120)
        text("Play",'segoe ui',40,white,188,220)
        text("Scenery",'segoe ui',40,white,x,270)
        clock.tick(60)
        pygame.display.update()  

    for x in range(-200,185,40):
        window.fill(black)
        text("Quick Taps",'segoe ui',60,white,90,120)
        text("Play",'segoe ui',40,white,188,220)
        text("Scenery",'segoe ui',40,white,158,270)
        text("Help",'segoe ui', 40, white, x,320)
        clock.tick(60)
        pygame.display.update()     

def endscreen_anim():

    s = pygame.Surface((window_width,window_height))

    for x in range(0,180,5):
        window.blit(bg,(0,0))
        s.set_alpha(x)
        s.fill((180,0,0))
        window.blit(s,(0,0))
        clock.tick(60)
        pygame.display.update()

    for x in range(-200,178,40):
        window.blit(bg,(0,0))
        window.blit(s,(0,0))
        text("Retry",'segoe ui',40,white,x,160)
        clock.tick(60)
        pygame.display.update()

    for x in range(-200,175,40):
        window.blit(bg,(0,0))
        window.blit(s,(0,0))
        text("Retry",'segoe ui',40,white,178,160)
        text("Menu",'segoe ui',40,white,x,220)
        clock.tick(60)
        pygame.display.update()  

def randomize_bg():
    global random_bg, bg_used, bg_list, bg
    if random_bg:
        if len(bg_used) == len(bg_list)-1: # -1 because of centre piece
            bg_used = []
        while True:
            bg = bg_list[random.randint(0,len(bg_list)-1)]
            if bg != bg_list[4] and bg not in bg_used:
                bg_used.append(bg)
                break

if (__name__ == "__main__"):

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Quick Taps")

    GAME_STATE = title
    GAME_MODE = None

    active_object_list = pygame.sprite.Group()

    pad_pos = []

    pad1 = Pad()
    pad1.set_pos()
    pad2 = Pad()
    pad2.set_pos()
    pad3 = Pad()
    pad3.set_pos()

    active_object_list.add(pad1,pad2,pad3)

    ACTION_CLICK = None
    ACTION_HOVER = None
    CLICK = False

    score = 0
    winscore = 20
    starttime = False
    time = 0

    random_bg = True
    bg_used = []

    winscreen_alpha = 255

    while 1:

        while (GAME_STATE == title):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                    GAME_STATE = menu
                    menu_anim()
            
            if GAME_STATE != title:
                break

            window.fill(black)

            text("Quick Taps",'segoe ui',60,white,90,180)

            clock.tick(60)
            
            winscreen_alpha = 255

            pygame.display.update()

        while (GAME_STATE == menu):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    CLICK = True

            if ACTION_CLICK == "1":
                GAME_STATE = game
                GAME_MODE = arcade
                randomize_bg()

            elif ACTION_CLICK == "2":
                GAME_STATE = bg_select
            elif ACTION_CLICK == "3":
                GAME_STATE = help_screen

            window.fill(black)

            text("Quick Taps",'segoe ui',60,white,90,120)
            if ACTION_HOVER == "h1":
                text("Play",'segoe ui',40,white,190,220)
            text("Play",'segoe ui',40,white,188,220)
            if ACTION_HOVER == "h2":
                text("Scenery",'segoe ui',40,white,160,270)    
            text("Scenery",'segoe ui',40,white,158,270)
            if ACTION_HOVER == "h3":
                text("Help",'segoe ui', 40, white, 187,320)
            text("Help",'segoe ui', 40, white, 185,320)

            button(178,230,90,40,"h1","1")
            button(158,280,120,40,"h2","2")
            button(185,330,70,40,"h3","3")

            CLICK = False

            clock.tick(60)
            pygame.display.update()

        while (GAME_STATE == help_screen):
            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    CLICK = True

            if ACTION_CLICK == "1":
                GAME_STATE = menu
                
            window.fill(black)

            window.blit(help_bg, (0,0))

            mouse = pygame.mouse.get_pos()

            if ACTION_HOVER == "h1":
                text("Back",'segoe ui',40,white,190,360)
            text("Back",'segoe ui',40,white,188,360)

            button(178,360,90,50,"h1","1")

            CLICK = False

            clock.tick(60)
            pygame.display.update()

        while (GAME_STATE == bg_select):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if ACTION_HOVER == 4:
                        random_bg = True
                    else:
                        bg = bg_list[ACTION_HOVER]
                        random_bg = False
                    GAME_STATE = menu
                    bg_used = []

            window.fill(black)

            mouse = pygame.mouse.get_pos()

            for row in range(3):
                for col in range(3):
                    window.blit(pygame.transform.scale(bg_list[row+col*3], (130,130)),(row*148+12,col*148+12))
                    if row*148+12 + 130 > mouse[0] and mouse[0] > row*148+12 \
                    and col*148+12 + 130 > mouse[1] and mouse[1] > col*148+12:
                        ACTION_HOVER = row+col*3
                    else:
                        cover = pygame.Surface((130,130));cover.set_alpha(100);cover.fill(black)
                        window.blit(cover, (row*148+12,col*148+12))

            clock.tick(fps)
            pygame.display.update()

        while (GAME_STATE == game):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if (event != None):
                    if (event.type == pygame.KEYDOWN):
                        if event.key == K_p:
                            GAME_STATE = paused
                            s = pygame.Surface((window_width,window_height))  
                            s.set_alpha(200)               
                            s.fill(black)          
                            window.blit(s, (0,0))    
                            text("PAUSED",'segoe ui',40,white,160,190)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        CLICK = True
                        starttime = True
                        if mouse_collide(pad1,pygame.mouse.get_pos()) == False \
                        and mouse_collide(pad2,pygame.mouse.get_pos()) == False \
                        and mouse_collide(pad3,pygame.mouse.get_pos()) == False:
                            GAME_STATE = endscreen
                            endscreen_anim()
                            reset()
                            
            if GAME_STATE != game:
                break

            pad1.mouse,pad2.mouse,pad3.mouse = pygame.mouse.get_pos(),pygame.mouse.get_pos(),pygame.mouse.get_pos()

            active_object_list.update()

            screen_fade = pygame.Surface((window_width,window_height));screen_fade.set_alpha(60);screen_fade.fill(white)

            window.blit( bg, (0,0))
            window.blit( screen_fade, (0,0) )
            active_object_list.draw(window)

            text(str(score),"segoe ui",50,black,395,10)

            if GAME_MODE == arcade:
                if score == winscore:
                    GAME_STATE = winscreen
                if starttime:
                    time += 1

            CLICK = False

            clock.tick(fps)
            pygame.display.update()

        while (GAME_STATE == paused):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    if event.key == K_p:
                        GAME_STATE = game

            clock.tick(fps)
            pygame.display.update()

        while (GAME_STATE == endscreen):

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    CLICK = True

                if (event.type == pygame.KEYDOWN):
                    if GAME_MODE == arcade:
                        reset()
                        GAME_STATE = game
                        randomize_bg()
                        

            window.blit(bg,(0,0))
            s = pygame.Surface((window_width,window_height))
            s.set_alpha(180)
            s.fill((180,0,0))
            window.blit(s,(0,0))

            if ACTION_HOVER == "h1":
                text("Retry",'segoe ui',40,white,180,160)
            text("Retry",'segoe ui',40,white,178,160)
            if ACTION_HOVER == "h2":
                text("Menu",'segoe ui',40,white,177,220)
            text("Menu",'segoe ui',40,white,175,220)

            button(178,170,90,40,"h1","a")
            button(175,230,100,40,"h2","b")

            if ACTION_CLICK == "a":
                if GAME_MODE == arcade:
                    reset()
                    GAME_STATE = game
                randomize_bg()
            elif ACTION_CLICK == "b":
                menu_anim()
                GAME_STATE = menu
            CLICK = False

            clock.tick(fps)
            pygame.display.update()

        while (GAME_STATE == winscreen):

            endtime = str(int(time/60))+":"+str(int(time/6))
            message = segoe72.render(endtime, True,black)

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                    GAME_STATE = title
                    reset()

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







































