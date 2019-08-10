import pygame
import random
from project.constants import ECRAN

#(self.rect.left, self.rect.top)

class Boss(pygame.sprite.Sprite):
    vitesse = 1
    vie = 7
    animcycle = 12
    images = []
    direction = 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midright=(ECRAN.width, random.random() * (ECRAN.height - self.image.get_height()) + self.image.get_height() / 2))
        self.frame = 0
        
    def update(self):
        self.rect.move_ip(-self.vitesse, self.direction)
        if self.rect.left <= -self.rect.width:
            self.kill()
            
        self.frame = self.frame + 1
        if (self.frame%15==0):
            self.direction=-self.direction
        if (self.frame%30==0):
            Tir_boss(self.gunpos())
            Tir_boss_haut(self.gunpos())
            Tir_boss_bas(self.gunpos())
    
    def impact(self):
        self.vie-=1
        
    
    def gunpos(self):
        return self.rect.left, self.rect.centery


class Tir_boss(pygame.sprite.Sprite):
    vitesse = 15
    
    def __init__(self, gunpos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=gunpos)

    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        if self.rect.right < 0 :
            self.kill()

class Tir_boss_haut(pygame.sprite.Sprite):
    vitesse = 15
    
    def __init__(self, gunpos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=gunpos)

    def update(self):
        self.rect.move_ip(-self.vitesse, self.vitesse)
        if self.rect.right < 0 :
            self.kill()

class Tir_boss_bas(pygame.sprite.Sprite):
    vitesse = 15
    
    def __init__(self, gunpos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=gunpos)

    def update(self):
        self.rect.move_ip(-self.vitesse, -self.vitesse)
        if self.rect.right < 0 :
            self.kill()