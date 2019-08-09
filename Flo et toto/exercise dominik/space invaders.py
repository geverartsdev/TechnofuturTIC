import pygame
import random
#dimesion fenetre#
largeur=650
hauteur=700
#police#
pygame.font.init()
ma_police=pygame.font.SysFont('Comic Sans MS',30)

ecran=pygame.display.set_mode((largeur,hauteur))
clock=pygame.time.Clock()
FPS=20
#Couleurs RGB (rouge vert bleu)#
White=(180,238,180)
Green=(0,255,0)
Black=(0,0,0)
Red=(255,0,0)

#vaisseau#
vaisseau=[[largeur//2,690]]
taille=10
speed=5
x=0
#alien#
spe=1
aliens = []
xal=spe
descendre = False
#bunker#
bunker = []
#tir#
tir_a= []
tira_x= None
tira_y= None
tirv_x= None
tirv_y= None
#score
score=0
def tirv():
    global tirv_x, tirv_y
    tirv_x = vaisseau[0][0]
    tirv_y = vaisseau[0][1] - 10
def tira():
    global tira_x, tira_y
    tira_x = aliens[i][j][0]
    tira_y = aliens[i][j][1]
def generate_aliens():
    global aliens
    aliens = []
    for line in range(0,5):
        aliens.append([])
        for j in range (0,11):
            aliens[line].append([100 + j*45,100 + line * 45])
    
def generate_bunker():
    global bunker
    for line in range(0,4):
        bunker.append([70 + line * 140, 550 ])
generate_bunker()

generate_aliens() 
game_over=3
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            #changement de direction#
            if event.key == pygame.K_LEFT :
                x=-speed
            elif event.key == pygame.K_RIGHT :
                x=speed
            elif event.key == pygame.K_DOWN:
                x=0
            elif event.key == pygame.K_SPACE:
                tirv()
            
            elif event.key == pygame.K_r:
                x=0
                vaisseau=[[largeur/2,650]]
                game_over =3
                generate_aliens()
                spe=1
            
    
    ecran.fill(Black)
    if game_over!=0:
        
        #mise a jouer des position du vaisseau#
        if (vaisseau[0][0] + x < 0 or vaisseau[0][0] + x > largeur-taille) :
           x=0
           vaisseau.insert(0,[vaisseau[0][0],vaisseau[0][1]])
           vaisseau.pop()
        elif x != 0:
            vaisseau.insert(0,[vaisseau[0][0]+x,vaisseau[0][1]])
            vaisseau.pop()
        #collision Murs#
        if (aliens [0][0][0]+x<0):
            spe +=1
            xal=1
            descendre = True
            
        elif(aliens [0][-1][0]+x>largeur-(taille*2)):
            spe += 1
            if spe > 10:
                spe = 10
            xal=-1
            descendre = True
        #collision tir_a
        
            
        #collision tir_v
        if tirv_x is not None:
            collide = False
            tmp = []
            for i in range(0,len(aliens)):
                tmp.append([])
                for j in range(0, len(aliens[i])):
                    if not(aliens[i][j][0] <= tirv_x and tirv_x <= (aliens[i][j][0] + 20) and aliens[i][j][1] <= tirv_y and tirv_y <= (aliens[i][j][1] + 20)):
                        tmp[-1].append(aliens[i][j])
                    else:
                        score+=10
                        collide = True
                        
                        
            aliens = tmp
            if collide is True:
                tirv_x = None
            
        #DESSINS ALIENS
        for i in range(0,len(aliens)):
            for j in range(0, len(aliens[i])):
                aliens[i][j][0] += (xal*spe)
                if descendre == True:
                    aliens[i][j][1] += 10
                if aliens[i][j][1] >= 510:
                    game_over = 0
                pygame.draw.rect(ecran,White,(aliens[i][j][0],aliens[i][j][1],taille*2,taille*2))
        descendre = False
        
        #DESSINS TIRS V
        if tirv_x is not None:
            tirv_x
            tirv_y -= 20
            if tirv_y <= 0:
                tirv_x = None
            else:
                pygame.draw.rect(ecran,Green,(tirv_x, tirv_y,taille//2,taille))
        
        #DESSINS TIRS A
        for i in range(0,len(tir_a)):
            pygame.draw.rect(ecran,White,(tir_a[i][0], tir_a[i][1],taille//2,taille))
        
        #dessin bunker
        for i in range(0,len(bunker)):
            pygame.draw.rect(ecran,Green,(bunker[i][0],bunker[i][1],taille*6,taille*4))
        #dessin vaisseau#
        for i in range(len(vaisseau)):
            pygame.draw.rect(ecran,Green,(vaisseau[i][0],vaisseau[i][1],taille*2,taille))
        
        
        #mise a jour ecran#
        textsurface=ma_police.render("score"+str(score),True,Red)
        ecran.blit(textsurface,(largeur//2,50))
    elif game_over==0:
        textsurface=ma_police.render("GAME OVER",False,Red)
        ecran.blit(textsurface,(largeur//2,hauteur//2))
        
    pygame.display.update()