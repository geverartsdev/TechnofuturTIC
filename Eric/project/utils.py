import os
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(fichier):
    """loads an image, prepares it for play"""
    fichier = os.path.join(main_dir, 'src/img', fichier)
    try:
        surface = pygame.image.load(fichier)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (fichier, pygame.get_error()))
    return surface.convert()


def load_images(*fichiers):
    imgs = []
    for fichier in fichiers:
        imgs.append(load_image(fichier))
    return imgs


class dummysound:
    def play(self): pass


def load_sound(fichier):
    if not pygame.mixer:
        return dummysound()
    fichier = os.path.join(main_dir, 'src/sound', fichier)
    try:
        sound = pygame.mixer.Sound(fichier)
        return sound
    except pygame.error:
        print('Warning, unable to load, %s' % fichier)
    return dummysound()
