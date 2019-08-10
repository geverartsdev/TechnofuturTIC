import pygame


class Bonus(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.kill()
