import pygame
from project.constants import ECRAN


class Menu(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()

    def update(self):
        pass