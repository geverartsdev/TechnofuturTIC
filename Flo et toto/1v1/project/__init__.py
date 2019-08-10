#!/usr/bin/env python3

import random

from project.utils import *
from project.HCSR04 import Sensor
from project.constants import *
from project.components.vaisseau import Vaisseau, Tir
from project.components.cowboy import Cowboy, Tire
from project.components.explosion import Explosion
from project.components.score import Score
from project.components.background import Background

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


main_dir = os.path.split(os.path.abspath(__file__))[0]


def images():
    """
    Cette methode s'occupe de charger et d'assigner les images au elements du jeu qui en ont besoin
    :return: ∅
    """
    v = load_image('vaiseau5.gif')
    Vaisseau.images =  [v, pygame.transform.flip(v, 1, 0)]   # le fichier utils.py
    c = load_image('cowboy3.gif')
    Cowboy.images = [c, pygame.transform.flip(c, 1, 0)]
    img = load_image('explosion4.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    b = load_image('meduse6.gif')
    Tir.images = [b, pygame.transform.flip(b, 1, 0)]
    t = load_image('munition1.gif')
    Tire.images = [t, pygame.transform.flip(t, 1, 0)]
    Background.image = load_image('fond4.jpg')


def fenetre():
    """
    Cette methode regle la fenetre de jeu, on choisit un titre, une icone, et on definit si on veut voir la souris
    apparaitre ou non
    :return: ∅
    """
    icon = pygame.transform.scale(Vaisseau.images[0], (32, 32))  # On utilise l'image de l'alien et on la redimensionne
    pygame.display.set_icon(icon)  # On definit une icone
    pygame.display.set_caption('Vacheline Invasion')  # On choisit le titre
    pygame.mouse.set_visible(0)  # On cache la souris

def main():
    """
    Fonction principale, appellee lors de l'execution du script
    :return: ∅
    """
    # Initialisation de pygame
    pygame.init()

    # Definit le mode de la fenetre
    winstyle = 0   # FULLSCREEN
    bestdepth = pygame.display.mode_ok(ECRAN.size, winstyle, 32)
    screen = pygame.display.set_mode(ECRAN.size, winstyle, bestdepth)

    # Chargement des images et assignement aux classes
    images()

    # Reglage de la fenetre
    fenetre()

    #sensor = Sensor()

    # On cree des groupes de jeu (un peu mystique, ce sont des listes qui vont garder une trace des differents elements
    # qui seront crees et qui les ajoutent automatiquement lors de leur creation)
    shots1 = pygame.sprite.Group()
    shots2 = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # On assigne a chaque classe un (ou des) groupe(s) qui lui correspond(ent)
    Background.containers = all
    Vaisseau.containers = all
    Cowboy.containers = all
    Tir.containers = shots1, all
    Explosion.containers = all
    Score.containers = all
    Tire.containers = shots2, all
    

    # On definit quelques valeurs de depart
    clock = pygame.time.Clock()

    # On initialise les elements du jeu, nous n'avons pas toujours besoin de garder une reference grace a l'utilisation
    # des containers, qui s'occupent de les recuperer lors de leur creation (plus de details dans les differents
    # elements)
    #Background(0)                             # On cree deux images de fond d'ecran, qui se suivent, pour qu'au moins
    #Background(Background.image.get_width())  # une se trouve a chaque fois visible par l'utilisateur
    player1 = Vaisseau() # On cree le joueur, on garde une reference pour pouvoir lui appliquer des actions
    player2 = Cowboy()

    

    score = Score()  # On cree le score, on garde une reference pour pouvoir le mettre a jour
    

    # Ici le jeu commence vraiment, dans cette boucle est defini toute la mecanique du jeu
    while player1.alive() and player2.alive():

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
        if keystate[pygame.K_s]:
            player1.move((0,1))
        elif keystate[pygame.K_z]:
            player1.move((0,-1))
        elif keystate[pygame.K_d]:
            player1.move((1,0))
        elif keystate[pygame.K_q]:
            player1.move((-1,0))
        firing = keystate[pygame.K_SPACE]
        if player1.alive() and not player1.reloading and firing and len(shots1) < MAX_TIRS1:
            Tir(player1.gunpos(), player1.direction)
        player1.reloading = firing

        if keystate[pygame.K_DOWN]:
            player2.move((0,1))
        elif keystate[pygame.K_UP]:
            player2.move((0,-1))
        elif keystate[pygame.K_RIGHT]:
            player2.move((1,0))
        elif keystate[pygame.K_LEFT]:
            player2.move((-1,0))
        firing = keystate[pygame.K_KP0]
        if player2.alive() and not player2.reloading and firing and len(shots2) < MAX_TIRS2:
            Tire(player2.gunpos(), player2.direction)
        player2.reloading = firing

        # Detection des collisions
        if pygame.sprite.collide_rect(player1, player2):
            Explosion(player2)
            Explosion(player1)
            score.point()
            player1.kill()
            player2.kill()

        for sh in pygame.sprite.spritecollide(player2, shots1, 1):
            Explosion(player2)
            score.point()
            player2.kill()
                
        for sh in pygame.sprite.spritecollide(player1, shots2, 1):
            Explosion(player1)
            score.point()
            player1.kill()
        
            

        # On dessine les elements
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # On definit le taux de rafraichissement de la fenetre
        clock.tick(30)  # La fenetre ne se rafraichira jamais plus de 30 fois par seconde

    # La partie est terminee, on affiche dans le terminal le score final
    if (player1.alive()):
        print("Bravo mon vionvion")
    elif (player2.alive()):
        print("Bravo mon COW boy")
    else:
        print("EGALITE")
        
    pygame.quit()


# appelle la fonction main si on execute le script
if __name__ == '__main__':
    main()

