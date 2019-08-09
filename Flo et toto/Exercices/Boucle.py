import random

reussi = False


def jeux(i, b):
    if (i==b):
        print("Tu as réussi ")
        reussi = True
    else:
        input("Faux")

        
while(not reussi):
    i = random.randint(1,100)
    b = input("Trouve un nombre entre 1 à 100 :")


    jeux(i, int(b))
    
