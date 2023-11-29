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

player = Player(all_sprites, enemies) # LAGER 1 KOPI AV PLAYER
enemy = Enemy()

image = pg.image.load('mbg.png')
def Background_sky(image):
    size = pg.transform.scale(image, (1200,800))
    screen.blit(size, (0, 0))


all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

pos_x = 100
pos_y = 100








i = 0
playing = True
while playing:
    clock.tick(60)
    #print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()



    
   

    hits = pg.sprite.spritecollide(player, enemies, False)
    if hits:
        print("collided with enemies")

    all_sprites.update()
    enemies.update()

    

    Background_sky(image)

    all_sprites.draw(screen)


    


    pg.display.update()
