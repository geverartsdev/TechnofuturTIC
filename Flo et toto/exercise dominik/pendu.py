mot= input("choisissez un mot")
for i in range (1,40):
    print(" ")
x=10
def pendu(mot,x):
    if x==0 :
        print("perdu")
    elif rep == etoiles:
        print ("victoir")
    else :
        etoiles = ""
        print(x)
        rep=""
        for letter in mot:
            etoiles += "*"
        print(etoiles)
        y=input("choisissez une lettre")
        for letter in mot:
            if letter == y:
                print("bravo")
                rep+="*"
                pendu(mot,x)
                
            elif letter != y :
                print("reessayer")
                x-=1
                pendu(mot,x)
       
pendu(mot,x)