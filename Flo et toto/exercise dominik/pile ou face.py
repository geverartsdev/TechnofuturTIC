from random import *

answer=input("pile(P) ou face(F) ?")

def pile_face(answer):
    result = randint(0,1)
    
    if (result == 0 and answer == "P") or (result == 1 and answer == "F"):
        print("gagner")
    else:
        print("perdu")
        
pile_face(answer)