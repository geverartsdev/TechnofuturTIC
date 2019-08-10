import pygame
import random
from project.constants import ECRAN


class Alien(pygame.sprite.Sprite):
    vitesse = 7
    animcycle = 12
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midright=(ECRAN.width, random.random() * (ECRAN.height - self.image.get_height()) + self.image.get_height() / 2))
        self.frame = 0

    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        if self.rect.left <= -self.rect.width:
            self.kill()
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 1]
