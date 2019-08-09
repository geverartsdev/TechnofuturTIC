def presentation():
    prenom=input("quel est votre prenom?")
    nom=input("quel est votre nom?")
    age=input("quel est votre age?")
    print(prenom,nom,age)

import math
def Vol_sphere(r):
    v=4/3*math.pi*r**3
    return v

print(Vol_sphere(5))