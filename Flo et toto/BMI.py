Poids = int(input("Entrez votre poids : "))
Taille = float(input("Entrez votre taille : "))
BMI = Poids/(Taille*Taille)


if(BMI < 20):
    print("Votre BMI est inférieur a la moyenne " + "(" + str(BMI) + ")")
    
elif(BMI > 30):
        print("Votre BMI est supérieur a la moyenne " + "(" + str(BMI) + ")")
        
else:
    print("Votre BMI est dans la moyenne " + "(" + str(BMI) + ")")
        
              
