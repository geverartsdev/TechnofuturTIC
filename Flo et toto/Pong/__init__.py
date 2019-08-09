#!/usr/bin/env python3

import os
import random

from Pong.utils import *
from Pong.constants import *
from Pong.components.balle import Balle
from Pong.components.paddle import Paddle
from Pong.components.background import Background
from Pong.components.score import Score

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


main_dir = os.path.split(os.path.abspath(__file__))[0]
sound_list = list()
sound_list.append("sound1.wav")
sound_list.append("sound2.wav")
sound_list.append("sound3.wav")
sound_list.append("sound4.wav")


def images():
    """
    Cette methode s'ocupe de charger et d'assigner les images au elements du jeu
    :return: ∅
    """
    Balle.image = load_image('balle.gif')
    Paddle.images = [load_image('paddle1.gif'), load_image('paddle2.gif')]
    Background.image = pygame.transform.scale(load_image('background.jpeg'), (ECRAN.width, ECRAN.height))
    

def fenetre():
    """
    Cette methode regle la fenetre de jeu, on choisit un titre, une icone, et on definit si on veut voir la souris
    apparaitre ou non
    :return: ∅
    """
    icon = pygame.transform.scale(load_image('icon.jpg'), (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PONG 2.0')
    pygame.mouse.set_visible(1)

def game(screen):
     # On cree des groupes de jeu (un peu mystique, ce sont des listes qui vont
    #garder une trace des differents elements
    # qui seront crees et qui les ajoutent automatiquement lors de leur
    #creation)
    balle = pygame.sprite.GroupSingle()
    paddles = pygame.sprite.Group()
    back = pygame.sprite.RenderUpdates()
    all = pygame.sprite.RenderUpdates()

    # On assigne a chaque classe un (ou des) groupe(s) qui lui correspond(ent)
    #Background.containers = all
    #¼Background.containers = all, back
    Paddle.containers = all, paddles
    Balle.containers = all, balle
    Score.containers = all

    # On definit quelques valeurs de depart
    clock = pygame.time.Clock()
    
    # On initialise les elements du jeu, nous n'avons pas toujours besoin de garder une reference grace a l'utilisation
    # des containers, qui s'occupent de les recuperer lors de leur creation (plus de details dans les differents
    # elements)
    #Background(0)                             # On cree deux images de fond d'ecran, qui se suivent, pour qu'au moins
    #Background(Background.image.get_width())  # une se trouve a chaque fois visible par l'utilisateur
    player1 = Paddle(True)# On cree le joueur, on garde une reference pour pouvoir lui appliquer des actions
    player2 = Paddle(False)
    score1 = Score(True)
    score2 = Score(False)
    ball = Balle(score1,score2)
    # Background(0)
    # Ici le jeu commence vraiment, dans cette boucle est defini toute la
    # mechanique du jeu
    while player1.alive() and player2.alive():

        randomMusic()
        
        #get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

        keystate = pygame.key.get_pressed()

        # On efface le contenu de l'ecran
        #all.clear(screen, pygame.Surface(ECRAN.size))

         # On rafraichit tous les elements
        all.update()

        # On reagit aux actions du joueur
        if keystate[pygame.K_s]:
            player1.move(1)
        if keystate[pygame.K_z]:
            player1.move(-1)
        if keystate[pygame.K_DOWN]:
            player2.move(1)
        if keystate[pygame.K_UP]:
            player2.move(-1)

        # Detection des collisions
        if pygame.sprite.collide_rect(player1, ball):
            rebony = (ball.rect[1] + ball.rect[3]/2) - (player1.rect[1] + player1.rect[3]/2)
            ball.rebon(True,rebony/20)
        if pygame.sprite.collide_rect(player2, ball):
            rebony =(ball.rect[1] + ball.rect[3]/2) - (player2.rect[1] + player2.rect[3]/2) 
            ball.rebon(True,rebony/20)

        # On dessine les elements
        screen.blit(Background.image, ECRAN)
        
        dirty = all.draw(screen)
        pygame.display.update()

        # On definit le taux de rafraichissement de la fenetre
        clock.tick(30)
    
def randomMusic():
    if pygame.mixer and SONS and not pygame.mixer.music.get_busy():
        music = os.path.join(main_dir, 'src/sound', sound_list[random.randint(0,3)])
        
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

        
def sons():
    """
    Cette methode s'occupe de charger les sons du jeu et lance la musique principale
    :return:
    """
    if pygame.mixer and SONS:
        music = os.path.join(main_dir, 'src/sound', '')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    
def main():
    
    # Initialisation de pygame
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None
        
    # Definit le mode de la fenetre
    winstyle = 0 #FULLSCREEN
    bestdepth = pygame.display.mode_ok(ECRAN.size, winstyle, 32)
    screen = pygame.display.set_mode(ECRAN.size, winstyle, bestdepth)

    # Chargement des images et assignement aux classes.
    images()


    while menu (screen):
        game(screen)

    # Reglage de la fenetre
    fenetre()

    # La partie est terminee
    pygame.quit()

def menu (screen):
    clock = pygame.time.Clock()
    screen.blit(pygame.transform.scale(load_image('balle.gif'), (ECRAN.width, ECRAN.height)), ECRAN)
    pygame.display.update()
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_SPACE]:
            return 1
        elif keystate[pygame.K_q]:
            return 0
        clock.tick(30)

# appelle la fonction main si on execute le script
if __name__ == '__main__':
    main()

        
            

        


    
    
    
    



    
