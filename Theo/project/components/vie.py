import pygame
from pygame.locals import Color


class Vie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('red')
        self.valeur = 3
        self.modif = True
        self.update()
        self.rect = self.image.get_rect().move(30, 30)

    def point(self):
        self.valeur += 1
        self.modif = True

    def lose(self):
        self.valeur -= 1
        self.modif = True

    def vie(self):
        return self.valeur

    def update(self):
        if self.modif:
            msg = "Vie : " + str(self.valeur)
            self.image = self.font.render(msg, 0, self.color)
            self.modif = False
