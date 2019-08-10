import pygame
from project.constants import ECRAN

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Spacecraft
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Vaisseau(pygame.sprite.Sprite):
    speed = 20

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=ECRAN.midleft, centerx=200)
        self.reloading = 0
        self.life = 3

    def move(self, direction):
        dirx, diry = direction
        self.rect.move_ip(dirx * self.speed, diry * self.speed)
        self.rect = self.rect.clamp(ECRAN)

    def gunpos(self):
        return self.rect.right, self.rect.centery

    def loselive(self):
        self.life -= 1
        if (self.life == 0):
            self.kill()

    def vie(self):
        self.life += 1

class Tir(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=pos)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > ECRAN.width:
            self.kill()
