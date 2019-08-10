import pygame
from pygame.locals import Color
from Pong.constants import ECRAN


class Score(pygame.sprite.Sprite):
    color = Color('green')
    
    def __init__(self, left):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.Font(None, 30)
        self.font.set_italic(1)
        self.valeur = 0
        self.modif = True
        self.update()
        if left == True :
            self.rect = self.image.get_rect(right=ECRAN.width/2 - 40, top=10)
            self.color = Color('red')
        else:
            self.rect = self.image.get_rect(left=ECRAN.width/2 + 40, top=10)
            self.color = Color('blue')
        self.modif = True
        self.update()


    def point(self):
        self.valeur += 1
        self.modif = True

    def score(self):
        return self.valeur

    def update(self):
        if self.modif:
            msg = "Score: " + str(self.valeur)
            self.image = self.font.render(msg, 0, self.color)
            self.modif = False
