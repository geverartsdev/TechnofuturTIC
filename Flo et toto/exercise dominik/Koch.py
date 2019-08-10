from turtle import *
koch1= Turtle()
koch1.backward(100)
def koch (x):
    if x<10:
        koch1.forward(x)
    else :
        koch(x/3)
        koch1.left(60)
        koch(x/3)
        koch1.right(120)
        koch(x/3)
        koch1.left(60)
        koch(x/3)
koch(300)
koch1.left(120)
koch(300)
koch1.left(120)
koch(300)