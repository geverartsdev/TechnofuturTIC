from random import *
number=randint(1,100)
x=0
def plus_moins(number,x):
    find= int(input("entrez votre nombre"))
    x+=1
    if x==8:
        print("perdu")
    elif number==find:
        print("gagne")
    elif find < number:
        print("c'est plus")
        plus_moins(number,x)
    elif find> number :
        print ("c'est moins")
        plus_moins(number,x)

plus_moins(number,x)  