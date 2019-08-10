import pygame
import random
from project.constants import ECRAN


class Boss(pygame.sprite.Sprite):
    vitesse = 0.5
    animcycle = 12
    images = []
    life = 50
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midright=(ECRAN.width, random.random() * (ECRAN.height - self.image.get_height()) + self.image.get_height() / 2))
        self.frame = 0
        
    def loselive(self):
        self.life -= 1
        if (self.life == 0):
            self.kill()
            
    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        
        
