#!/usr/bin/env python3

import random

from project.utils import *
from project.HCSR04 import Sensor
from project.constants import *
from project.components.vaisseau import Vaisseau, Tir
from project.components.alien import Alien
from project.components.explosion import Explosion
from project.components.score import Score

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


main_dir = os.path.split(os.path.abspath(__file__))[0]


def images():
    """
    Cette methode s'occupe de charger et d'assigner les images au elements du jeu qui en ont besoin
    :return: ∅
    """
    Vaisseau.image = load_image('spacecraft.gif')    # le fichier utils.py
    img = load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    Tir.image = load_image('shot.gif')


def fenetre():
    """
    Cette methode regle la fenetre de jeu, on choisit un titre, une icone, et on definit si on veut voir la souris
    apparaitre ou non
    :return: ∅
    """
    icon = pygame.transform.scale(Alien.images[0], (32, 32))  # On utilise l'image de l'alien et on la redimensionne
    pygame.display.set_icon(icon)  # On definit une icone
    pygame.display.set_caption('Pygame Aliens')  # On choisit le titre
    pygame.mouse.set_visible(0)  # On cache la souris

def main():
    """
    Fonction principale, appellee lors de l'execution du script
    :return: ∅
    """
    # Initialisation de pygame
    pygame.init()

    # Definit le mode de la fenetre
    winstyle = 0  # FULLSCREEN
    bestdepth = pygame.display.mode_ok(ECRAN.size, winstyle, 32)
    screen = pygame.display.set_mode(ECRAN.size, winstyle, bestdepth)

    # Chargement des images et assignement aux classes
    images()

    # Reglage de la fenetre
    fenetre()

    #sensor = Sensor()

    # On cree des groupes de jeu (un peu mystique, ce sont des listes qui vont garder une trace des differents elements
    # qui seront crees et qui les ajoutent automatiquement lors de leur creation)
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    # On assigne a chaque classe un (ou des) groupe(s) qui lui correspond(ent)
    #Background.containers = all
    Vaisseau.containers = all
    Alien.containers = aliens, all, lastalien
    Tir.containers = shots, all
    Explosion.containers = all
    Score.containers = all

    # On definit quelques valeurs de depart
    alien_suivant = NOUVEL_ALIEN
    clock = pygame.time.Clock()

    # On initialise les elements du jeu, nous n'avons pas toujours besoin de garder une reference grace a l'utilisation
    # des containers, qui s'occupent de les recuperer lors de leur creation (plus de details dans les differents
    # elements)
    #Background(0)                             # On cree deux images de fond d'ecran, qui se suivent, pour qu'au moins
    #Background(Background.image.get_width())  # une se trouve a chaque fois visible par l'utilisateur
    player = Vaisseau()  # On cree le joueur, on garde une reference pour pouvoir lui appliquer des actions
    score = Score()  # On cree le score, on garde une reference pour pouvoir le mettre a jour
    Alien()  # On cree un premier alien

    # Ici le jeu commence vraiment, dans cette boucle est defini toute la mecanique du jeu
    while player.alive():

        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

        keystate = pygame.key.get_pressed()

        # On efface le contenu de l'ecran
        all.clear(screen, pygame.Surface(ECRAN.size))

        # On rafraichit tous les elements
        all.update()

        # On reagit aux actions du joueur
        #dirx = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        #diry = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
        #player.move((dirx, diry))
        if keystate[pygame.K_UP]:
            player.move((0,1))
        else:
            player.move((0,-1))
        firing = keystate[pygame.K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_TIRS:
            Tir(player.gunpos())
        player.reloading = firing

        # Creation (eventuelle) d'un nouvel alien
        if alien_suivant > 0:
            alien_suivant = alien_suivant - 1
        elif len(aliens) <= MAX_ALIEN and not int(random.random() * PROBA_ALIEN):
            Alien()
            alien_suivant = NOUVEL_ALIEN

        # Detection des collisions
        for alien in pygame.sprite.spritecollide(player, aliens, 1):
            Explosion(alien)
            Explosion(player)
            score.point()
            player.kill()

        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            Explosion(alien)
            score.point()

        # On dessine les elements
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # On definit le taux de rafraichissement de la fenetre
        clock.tick(30)  # La fenetre ne se rafraichira jamais plus de 30 fois par seconde

    # La partie est terminee, on affiche dans le terminal le score final
    print("Final score = " + str(score.score()))

    pygame.quit()


# appelle la fonction main si on execute le script
if __name__ == '__main__':
    main()

