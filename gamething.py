import pygame as pg
from sprites import *
pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen = pg.display.set_mode((1200,800))

clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

player = Player(all_sprites, enemies)
enemy = Enemy()


all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

pos_x = 100
pos_y = 100

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT




i = 0
playing = True
while playing:
    clock.tick(165)
    #print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()

    keys_pressed = pg.key.get_pressed()

    if keys_pressed[pg.K_SPACE]:
        jumping = True

    hits = pg.sprite.spritecollide(player, enemies, False)
    if hits:
        print("collided with enemies")

    all_sprites.update()
    enemies.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    if jumping:
        pos_y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT



    pg.display.update()
