import pygame
import random
from project.constants import ECRAN


class Heal(pygame.sprite.Sprite):
    vitesse = 7
    animcycle = 12
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midright=(ECRAN.width, random.random() * (ECRAN.height - self.image.get_height()) + self.image.get_height() / 2))

    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        if self.rect.left <= -self.rect.width:
            self.kill()