import pygame
from project.constants import ECRAN

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Spacecraft
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard

class Tirs(pygame.sprite.Sprite):
    speed = 50

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midleft=pos)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > ECRAN.width:
            self.kill()