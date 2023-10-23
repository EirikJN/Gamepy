import pygame as pg
import random

player_image = pg.image.load("Duck_Sprite.png")
enemy_image = pg.image.load("Duck_Sprite.png")

class Player(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 3

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        if self.pos_x < 0:
            self.pos_x = 0 

        if self.pos_x > 1200:
            self.pos_x = 1200 

        if self.pos_y <0:
            self.pos_y = 0 

        if self.pos_y > 800:
            self.pos_y = 800 

        # player input
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            self.pos_y -= self.speed
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 

class Enemy(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 100
        self.pos_y = 100
        self.speed = 2

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        if self.pos_x < 0:
            self.pos_x = 0 

        if self.pos_x > 1200:
            self.pos_x = 1200 

        if self.pos_y <0:
            self.pos_y = 0 

        if self.pos_y > 800:
            self.pos_y = 800 

        # player input
        keys = pg.key.get_pressed()
        if keys[pg.K_i]: # oppover
            self.pos_y -= self.speed
        if keys[pg.K_k]: # nedover
            self.pos_y += self.speed
        if keys[pg.K_j]: # venstre
            self.pos_x -= self.speed
        if keys[pg.K_l]: # høyre
            self.pos_x += self.speed 