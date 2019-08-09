dict = {}
def voyelle(dict):
    dict["a"] = "a"
    dict["e"] = "e"
    dict["i"] = "i"
    dict["o"] = "o"
    dict["u"] = "u"
    dict["y"] = "y"

    
texte = input("Entrer votre texte :")

nouveauTexte = ""

voyelle(dict)
for lettre in texte:
    
    if(lettre in dict):
         nouveauTexte = nouveauTexte+lettre
print(nouveauTexte)
    
    
    
    
