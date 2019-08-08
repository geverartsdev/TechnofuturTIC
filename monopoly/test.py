import pygame,sys



pygame.init()

largeur, hauteur = 1240,880

ecran = pygame.display.set_mode((largeur, hauteur))


class Mechant:

    def __init__(self):
        self.image = pygame.image.load("gerbille.jpg")
        self.posH = largeur
        # self.rect[0] = positionHorizontale
        # self.rect[1]
        # self.rect[2] = largeur de l'image
        # self.rect[3] = hauteur de l'image
        self.rect = self.image.get_rect()
        self.posV = hauteur - self.rect[3]
        self.vitesse = -1


    def dessiner(self, ecran):
        ecran.blit(self.image, (self.posH, self.posV))
        self.posH = self.posH + self.vitesse

    def collision(joueur):
        if self.rect.colliderect(joueur.rect):
            joueur.kill()
            

class Joueur:
    def __init__(self):
        self.image = pygame.image.load("index.jpeg")
        self.posH = 0
        self.rect = self.image.get_rect()
        self.posV = hauteur - self.rect[3]
        
        self.vitesseVerticale = 0
        self.jumping = False
        self.vivant = True


    def dessiner(self, ecran):
        ecran.blit(self.image, (self.posH, self.posV))
        self.posV = self.posV - self.vitesseVerticale
    def kill():
        self.vivant=False



#Rouge, vert, bleu
BLANC = (255,255,255)
ROUGE = (255,0,0)
NOIR = (0,0,0)


playing = True
gravite = 0.1

mechant = Mechant()
joueur = Joueur()

while playing and joueur.vivant:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            playing = False

    clavieretat = pygame.key.get_pressed()

    if joueur.posV > hauteur - joueur.rect[3]:
        joueur.jumping = False
        joueur.posV = hauteur - joueur.rect[3]
        joueur.vitesseVerticale = 0
    
    if clavieretat[pygame.K_RIGHT]:
        joueur.posH = joueur.posH + 1
    elif clavieretat[pygame.K_LEFT]:
        joueur.posH = joueur.posH - 1
    if clavieretat[pygame.K_SPACE] and joueur.jumping == False:
        joueur.jumping = True
        joueur.vitesseVerticale = 10

    if joueur.jumping :
        joueur.vitesseVerticale = joueur.vitesseVerticale - gravite



    ecran.fill(NOIR)
    joueur.dessiner(ecran)
    mechant.dessiner(ecran)
    pygame.display.flip()

sys.exit()
