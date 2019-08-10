import pygame
from Pong.constants import ECRAN

class Background(pygame.sprite.Sprite):
    vitesse = 0

    def __init__(self, posx):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=(posx, ECRAN.midleft[1]))

    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        if self.rect.left <= -self.rect.width:
            self.rect.move_ip(self.rect.width * 2, 0)
