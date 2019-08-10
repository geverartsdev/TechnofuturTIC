import pygame
from Pong.components.score import Score
from Pong.constants import ECRAN

class Balle(pygame.sprite.Sprite):
    speed = 10
    dirx = 2
    diry = 0
    mort = 0
    ressuciter = 90

    def __init__(self,score1,score2):
        self.score1 = score1
        self.score2 = score2
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(centery=ECRAN.centery, centerx=ECRAN.centerx)

    def update (self):
        if self.mort > 0:
            self.mort -= 1
            return
        self.rect.move_ip(self.dirx * self.speed, self.diry * self.speed)
        if self.rect.bottom > ECRAN.bottom or self.rect.top < ECRAN.top:
            self.diry = -self.diry
            self.update()
        if self.rect.left < ECRAN.left or self.rect.right > ECRAN.right:
            if self.rect.left < ECRAN.left:
                self.score2.point()
            if self.rect.right > ECRAN.right:
                self.score1.point()
            self.rect = self.image.get_rect(centery=ECRAN.centery, centerx=ECRAN.centerx)
            self.dirx = -self.dirx
            self.mort = self.ressuciter

    def rebon (self, rebonx, rebony):
        if rebonx == True:
            self.dirx = -self.dirx
        self.diry = rebony

