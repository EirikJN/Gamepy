import pygame as pg
import random

player_image = pg.image.load("_Idle.png")
player_image = pg.transform.scale(player_image, (200,100))
enemy_image = pg.image.load("Duck_Sprite.png")
enemy_image = pg.transform.scale(enemy_image, (150,50))

ranged_image = pg.image.load("1_5.png")
ranged_imageimage = pg.transform.scale(ranged_image, (30,30))

class Player(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 3
        self.hp = 100

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y


    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
 
    def attack(self):
        projectile = Ranged_attack(self.pos_x, self.pos_y)
        print("attacked")
        projectile.add(self.all_sprites)

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
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 100
        self.pos_y = 100
        self.speed = 2
        
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

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

class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, x, y): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
 
        self.pos_x = x
        self.pos_y = y
        self.speed = 10
 
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

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