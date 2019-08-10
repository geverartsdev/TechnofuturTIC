import pygame

# Constantes de jeu
MAX_TIRS = 5  # nombre maximum de boulets sur l'ecran
MAX_ALIEN = 3
PROBA_ALIEN = 17  # probabilité qu'un alien apparaisse
PROBA_HEAL = 95# probabilité qu'un heal pack apparaisse
NOUVEL_ALIEN = 12   # Rafraichissement de l'ecran entre chaque alien
ECRAN = pygame.Rect(0, 0, 1750,900)
SONS = False  # Mettre a True si on veut activer le sons
