class Vache:
    
    nom = "Paula"
    nombrePates = 4
    couleur = "rose"
    vitesse = 0
    longueur = 3
    largeur = 2
    hauteur = 150
    distance = 0
    
    def __init__(self, nom, vitesse):
    
        self.nom = nom
        self.vitesse = vitesse

    def __str__(self):
        return self.nom + " " + str(self.vitesse)
    
    def setColor(self, couleur):
        self.couleur = couleur

    def courir(self, distance):
        self.distance += distance

        
vache = Vache("Popol", 15)
vache.setColor("mauve")
vache.courir(20)

print(vache)
print(vache.distance)
print(vache.couleur)
    
