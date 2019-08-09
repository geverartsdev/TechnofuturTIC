Nom = input("Entrer votre nom :")
Prenom = input("Entrer votre prenom :")
Age = input("Entrer votre âge :")

if (Age < str(18)):
    print("Désolé " + Prenom + " " + Nom + " mais vous n'avez pas l'âge requis pour "
          + "entrer sur ce site ^^")
else:
    print("Bienvenue " + Prenom + " " + Nom)
          
