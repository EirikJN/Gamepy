import pygame as pg

player_image = pg.image.load("Duck_Sprite.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 100
        self.pos_y = 100

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos_y -= 5

        if keys[pg.K_s]:
            self.pos_y += 5

        if keys[pg.K_a]:
            self.pos_x -= 5

        if keys[pg.K_d]:
            self.pos_x += 5