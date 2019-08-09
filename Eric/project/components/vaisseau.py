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
    speed = 10
    vies = 3
    dirx = 1
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft=ECRAN.midleft, centerx=200)
        self.reloading = 0

    def move(self, direction):
        dirx, diry = direction
        if (dirx!=0):
            self.dirx = dirx
            if (dirx==1):
                self.image = self.images[0]
            elif (dirx==-1):
                self.image = self.images[1]
        self.rect.move_ip(dirx * self.speed, diry * self.speed)
        self.rect = self.rect.clamp(ECRAN)
        
    def impact(self):
        self.vies-=1
        if (self.vies==0):
            self.kill()
    
    def healing(self):
        self.vies+=1

    def gunpos(self):
        if (self.dirx==1):
            return self.rect.right, self.rect.centery
        else:
            return self.rect.left, self.rect.centery

class Tir(pygame.sprite.Sprite):
    speed = 11

    def __init__(self, pos, dirx):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if (dirx==-1):
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect = self.image.get_rect(midright=pos)
        else:
            self.rect = self.image.get_rect(midleft=pos)
        self.dirx = dirx
        
    def update(self):
        self.rect.move_ip(self.speed*self.dirx, 0)
        if self.rect.left > ECRAN.width:
            self.kill()
        if self.rect.right < 0:
            self.kill()