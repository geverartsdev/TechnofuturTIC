L=int(input("Quel Longueur?"))
l=int(input("Quel largeur?"))
from turtle import *
def Rectangle(L,l):
    rectangle= Turtle()
    rectangle.forward(L)
    rectangle.right(90)
    rectangle.forward(l)
    rectangle.right(90)
    rectangle.forward(L)
    rectangle.right(90)
    rectangle.forward(l)
    
Rectangle(L,l)