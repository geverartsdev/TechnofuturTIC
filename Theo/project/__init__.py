
#!/usr/bin/env python3

import random

from project.utils import *
from project.HCSR04 import Sensor
from project.constants import *
from project.components.vaisseau import Vaisseau, Tir
from project.components.alien import Alien
from project.components.explosion import Explosion
from project.components.score import Score
from project.components.background import Background
from project.components.vie import Vie
from project.components.poce_blo import Poce
from project.components.bonus import Bonus
from project.components.boss import Boss
from project.components.tirsecondaire import Tirs
# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


main_dir = os.path.split(os.path.abspath(__file__))[0]


def images():
    """
    Cette methode s'occupe de charger et d'assigner les images au elements du jeu qui en ont besoin
    :return: ∅
    """
    Vaisseau.image = load_image('oie.png')    # le fichier utils.py
    img = load_image('kermite')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Alien.images = load_images('chat.jpg', 'chat.jpg', 'chat.jpg')
    Tir.image = load_image('shot.jpg')
    Poce.image = load_image('poce blo')
    Bonus.image = load_image('bonus')
    Boss.image = load_image('donaldo.jpeg')
    Tirs.image = load_image('agartha.JPG')
    Background.images = [pygame.transform.scale(load_image('piste.jpeg'),(ECRAN.width,ECRAN.height)),
                        pygame.transform.scale(load_image('strato.jpeg'),(ECRAN.width,ECRAN.height)),
                        pygame.transform.scale(load_image('espace.jpeg'),(ECRAN.width,ECRAN.height)),
                        pygame.transform.scale(load_image('hangar.jpeg'),(ECRAN.width,ECRAN.height))]
    #Background.image = load_image('téléchargement.jpeg')
    

def fenetre():
    """
    Cette methode regle la fenetre de jeu, on choisit un titre, une icone, et on definit si on veut voir la souris
    apparaitre ou non
    :return: ∅
    """
    icon = pygame.transform.scale(Alien.images[0], (32, 32))  # On utilise l'image de l'alien et on la redimensionne
    pygame.display.set_icon(icon)  # On definit une icone
    pygame.display.set_caption('Sylvain Durif contre les Chat de L ESPACE')  # On choisit le titre
    pygame.mouse.set_visible(0)  # On cache la souris

    def sons():
        if pygame.mixer and SONS:
            music = os.path.join(main_dir, 'alan-silvestri-portals-from-avengers-endgameaudio-only.mp3')
def game(screen):
    
    # On cree des groupes de jeu (un peu mystique, ce sont des listes qui vont garder une trace des differents elements
    # qui seront crees et qui les ajoutent automatiquement lors de leur creation)
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()
    poces = pygame.sprite.Group()
    donaldclub =pygame.sprite.GroupSingle()
    tirsseconds = pygame.sprite.Group()
    
    # On assigne a chaque classe un (ou des) groupe(s) qui lui correspond(ent)
    #
    #Background.containers = all
    Vaisseau.containers = all
    Alien.containers = aliens, all, lastalien
    Tir.containers = shots, all
    Explosion.containers = all
    Bonus.containers = all
    Score.containers = all
    Vie.containers = all
    Poce.containers = all, poces
    Boss.containers = all,donaldclub
    Tirs.containers = all,tirsseconds
    # On definit quelques valeurs de depart
    alien_suivant = NOUVEL_ALIEN
    clock = pygame.time.Clock()
    poce_suivant = NOUVEL_POCE

    # On initialise les elements du jeu, nous n'avons pas toujours besoin de garder une reference grace a l'utilisation
    # des containers, qui s'occupent de les recuperer lors de leur creation (plus de details dans les differents
    # elements)
    #Background(0)                             # On cree deux images de fond d'ecran, qui se suivent, pour qu'au moins
    #Background(Background.image.get_width())  # une se trouve a chaque fois visible par l'utilisateur
    player = Vaisseau()  # On cree le joueur, on garde une reference pour pouvoir lui appliquer des actions
    score = Score()  # On cree le score, on garde une reference pour pouvoir le mettre a jour
    Alien()  # On cree un premier alien
    vie = Vie()
    donvie = Poce()
    Background.image = Background.images[0]
    
    # Ici le jeu commence vraiment, dans cette boucle est defini toute la mecanique du jeu
    while player.alive():

        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

        keystate = pygame.key.get_pressed()

        # On efface le contenu de l'ecran
        # all.clear(screen, pygame.Surface(ECRAN.size))

        # On rafraichit tous les elements
        all.update()

        # On reagit aux actions du joueur
        #dirx = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        #diry = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
        #player.move((dirx, diry))
        if keystate[pygame.K_DOWN]:
            player.move((0,1))
        if keystate[pygame.K_UP]:
            player.move((0,-1))
        if keystate[pygame.K_LEFT]:
            player.move((-1,0))
        if keystate[pygame.K_RIGHT]:
            player.move((1,0))
        firing = keystate[pygame.K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_TIRS:
            Tir(player.gunpos())
        player.reloading = firing
        firing = keystate[pygame.K_LSHIFT]
        if not player.reloading and firing and len(shots) < MAX_TRISSECONDS:
            Tirs(player.gunpos())  
        # Creation (eventuelle) d'un nouvel alien
        if alien_suivant > 0:
            alien_suivant = alien_suivant - 1
        elif len(aliens) <= MAX_ALIEN and not int(random.random() * PROBA_ALIEN):
            Alien()
            alien_suivant = NOUVEL_ALIEN

        if poce_suivant > 0:
            poce_suivant = poce_suivant - 1
        elif len(poces) <= MAX_POCE and not int(random.random() * PROBA_POCE):
            Poce()
            poce_suivant = NOUVEL_POCE
            
        # Detection des collisions
        for alien in pygame.sprite.spritecollide(player, aliens, 1):
            Explosion(alien)
            Explosion(player)
            score.point()
            player.loselive()
            vie.lose()

        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            Explosion(alien)
            score.point()
            if score.valeur ==15:
                Background.image = Background.images[1]
            if score.valeur ==50:
                Background.image = Background.images[2]
            if score.valeur ==80:
                Background.image = Background.images[3]    
              
            if score.score() ==100:
                Boss()
                
        for donald in pygame.sprite.groupcollide(donaldclub, shots, 0, 1).keys():
            donald.loselive()
        
        for poce in pygame.sprite.spritecollide(player,poces,1):
            Bonus(poce)
            vie.point()
            player.vie()
            
        for alien in pygame.sprite.groupcollide(tirsseconds, aliens, 1, 1).keys():
            Explosion(alien)    
        # On dessine les elements
        screen.blit(Background.image,ECRAN)
        dirty = all.draw(screen)
        pygame.display.update()

        
                

        # On definit le taux de rafraichissement de la fenetre
        clock.tick(30)  # La fenetre ne se rafraichira jamais plus de 30 fois par seconde
    
    # La partie est terminee, on affiche dans le terminal le score final
    print("TON SCORE = " + str(score.score()))

def menu(screen):
    clock = pygame.time.Clock()
    screen.blit(pygame.transform.scale(load_image('menu12.png'), (ECRAN.width, ECRAN.height)), ECRAN)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
                
        keystate = pygame.key.get_pressed()
            
        if keystate[pygame.K_SPACE]:
            return 1
        elif keystate[pygame.K_q]:
            return 0
            
        clock.tick(30)

def main():
    """
    Fonction principale, appellee lors de l'execution du script
    :return: ∅
    """
    # Initialisation de pygame
    pygame.init()

    # Definit le mode de la fenetre
    winstyle = pygame.FULLSCREEN
    bestdepth = pygame.display.mode_ok(ECRAN.size, winstyle, 32)
    screen = pygame.display.set_mode(ECRAN.size, winstyle, bestdepth)

    # Chargement des images et assignement aux classes
    images()

    # Reglage de la fenetre
    fenetre()

    #sensor = Sensor()
    while menu(screen):
        game(screen)


    pygame.quit()


# appelle la fonction main si on execute le script
if __name__ == '__main__':
    main()

