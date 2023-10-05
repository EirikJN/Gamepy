import pygame as pg
from sprites import *
import random
pg.init() # starter pygame modul


 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
 
screen = pg.display.set_mode((800,600)) # lager spill vindu, 800x600
 
clock = pg.time.Clock()

player = Player()
 
pos_x = 100
pos_y = 100
size_x = 50
size_y = 50
box_1_dir = 5
 
pos_x2 = 600
pos_y2 = 100
size_x2 = 50
size_y2 = 50
box_2_dir = -5
 
i = 0
playing = True
while playing: # game loop
    clock.tick(120)
    #print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT: # hvis vi trykker på krysset i spillvinduet
            playing = False
            pg.quit()
 
    # player input
    keys = pg.key.get_pressed()
    if keys[pg.K_w]: # oppover
        pos_y -= 5
    if keys[pg.K_s]: # nedover
        pos_y += 5
    if keys[pg.K_a]: # venstre
        pos_x -= 5
    if keys[pg.K_d]: # høyre
        pos_x += 5 
 
    # player out of bounds, hold player på skjermen
    if pos_x < 0-size_x:
        pos_x = 0-size_x
        box_1_dir *= -1
    if pos_x2 > 800-size_x2:
        pos_x2 = 800-size_x2
        box_2_dir *= -1
    
    if pos_y < 0-size_y:
        pass
    if pos_y2 < 0-size_y2:
        pass
 
    screen.fill(YELLOW)
    
 
    player_box = pg.Rect(pos_x, pos_y, size_x,size_y)  # to første er posisjon, to siste er size
    pg.draw.rect(screen, RED, player_box)
    pos_x += box_1_dir # endrer posisjon x til playerboks med 1 pixel
   
    player_box2 = pg.Rect(pos_x2, pos_y2, size_x2,size_y2)  # to første er posisjon, to siste er size
    pg.draw.rect(screen, RED, player_box2)
    pos_x2 += box_2_dir # endrer posisjon x til playerboks med 1 pixel
   
    if pos_x > pos_x2:
        box_1_dir *= -1
        box_2_dir *= -1
 
    pg.display.update()