from random import *

answer=input("pile(P) ou face(F) ?")
str(answer)
def pile_face(answer):
    result = randint(0,1)
    P=0
    F=1
    if result == answer:
        print("gagner")
    else:
        print("perdu")
        print(result)
pile_face(answer)