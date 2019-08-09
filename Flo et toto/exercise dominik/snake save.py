import pygame
import random
#dimesion fenetre#
largeur=720
hauteur=480

#police#
pygame.font.init()
ma_police=pygame.font.SysFont('Comic Sans MS',30)

ecran=pygame.display.set_mode((largeur,hauteur))
clock=pygame.time.Clock()
FPS=20
#Couleurs RGB (rouge vert bleu)#
Green=(0,255,0)
Black=(0,0,0)
Red=(255,0,0)

#serpent#
serpent=[[largeur/2,hauteur/2]]
taille=10
speed=10
x=0
y=0
#pomme#
pomme_x=random.randint(1,(largeur-10)//10)*10
pomme_y=random.randint(1,(hauteur-10)//10)*10


game_over=0
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            #changement de direction#
            if event.key == pygame.K_LEFT and x==0:
                x=-speed
                y=0
            elif event.key == pygame.K_RIGHT and x==0:
                x=speed
                y=0
            elif event.key == pygame.K_UP and y==0:
                x=0
                y=-speed
            elif event.key == pygame.K_DOWN and y==0:
                x=0
                y=speed
            elif event.key==pygame.K_r:
                x=0
                y=0
                serpent=[[largeur/2,hauteur/2]]
                game_over =0
                
    ecran.fill(Black)
    if game_over==0:
        #collision Murs#
        if serpent[0][0]<0 or serpent[0][0]>largeur-taille or serpent[0][1]<0 or serpent[0][1]>hauteur-taille:
            game_over= 1
        #collision pomme#
        if serpent[0][0]== pomme_x and serpent[0][1] ==pomme_y:
            pomme_x=random.randint(1,(largeur-10)//10)*10
            pomme_y=random.randint(1,(hauteur-10)//10)*10
            #ajout queue du serpent#
            serpent.append([serpent[-1][0]+x,serpent[-1][1]+y])
        #mise a jouer des position du serpent#
            
        serpent.insert(0,[serpent[0][0]+x,serpent[0][1]+y])
        serpent.pop()
        
        #collision queue#
        if serpent[0] in serpent [1:]:
            game_over=1
            
        #mise a jour ecran#
        for i in range(len(serpent)):
            pygame.draw.rect(ecran,Green,(serpent[i][0],serpent[i][1],taille,taille))
        pygame.draw.rect(ecran,Red,(pomme_x,pomme_y,taille,taille))
    elif game_over==1:
        textsurface=ma_police.render("GAME OVER",False,Red)
        ecran.blit(textsurface,(largeur//2,hauteur//2))
        
    pygame.display.update()