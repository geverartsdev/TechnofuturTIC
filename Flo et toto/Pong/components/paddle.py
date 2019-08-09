import pygame
from Pong.constants import ECRAN

class Paddle(pygame.sprite.Sprite):
    speed = 20
    images = []
    
    def __init__(self, left):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if left == True :
            self.image = self.images[0]
            self.rect = self.image.get_rect(centery=ECRAN.centery, centerx=50)
        else:
            self.image = self.images[1]
            self.rect = self.image.get_rect(centery=ECRAN.centery, centerx=ECRAN.width-50)

    def move(self, diry):
        self.rect.move_ip(0, diry * self.speed)
        self.rect = self.rect.clamp(ECRAN)
        if self.rect.bottom > ECRAN.bottom:
            self.rect.move_ip(0, -self.speed)
        if self.rect.top < ECRAN.top:
            self.rect.move_ip(0, self.speed)
        


        
 
