from typing import Any
import pygame as pg
import random

player_image = pg.image.load("_Idle.png")
player_image = pg.transform.scale(player_image, (200,100))
enemy_image = pg.image.load("Duck_Sprite.png")
enemy_image = pg.transform.scale(enemy_image, (150,50))

ranged_image = pg.image.load("1_5.png")
ranged_imageimage = pg.transform.scale(ranged_image, (30,30))



class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 650
        self.speed = 10
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies = enemies

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        
        self.jumping = False
       
        self.left_image = pg.transform.flip(self.image,True,False)
        self.right_image = self.image

        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 20
        self.Y_VELOCITY = self.JUMP_HEIGHT
        

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
 
    #def attack(self):
        #projectile = Ranged_attack(self.pos_x, self.pos_y)
        #print("attacked")
        #projectile.add(self.all_sprites)

    def melee(self):
        meleeatt = MeleeAttack((100,100), self.enemies)
        self.all_sprites.add(meleeatt)


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
        
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
            
            self.image = self.left_image
            

        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 

            self.image = self.right_image
            
        
        if keys[pg.K_SPACE]:
            self.jumping = True
            
        if self.jumping:
            self.pos_y -= self.Y_VELOCITY
            self.Y_VELOCITY -= self.Y_GRAVITY
            if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                self.jumping = False
                self.Y_VELOCITY = self.JUMP_HEIGHT


class MeleeAttack(pg.sprite.Sprite):
    def __init__(self, position, enemies):
        super().__init__()
        self.image = pg.surface((20,20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=position)
        self.lifetime = 10

    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0: 
            self.kill()

        pg.sprite.spritecollide(self, self.enemies, True)

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