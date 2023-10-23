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

player = Player()

enemy = Enemy()

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
pos_x = 100
pos_y = 100

size_x = 100
sixe_y = 100



i = 0
playing = True
while playing:
    clock.tick(165)
    print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()


    all_sprites.update()
    enemies.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)



    pg.display.update()
