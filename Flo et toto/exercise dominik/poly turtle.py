from turtle import *
def rectangle():
    rectangle= Turtle()
    rectangle.forward(200)
    rectangle.right(90)
    rectangle.forward(60)
    rectangle.right(90)
    rectangle.forward(200)
    rectangle.right(90)
    rectangle.forward(60)
def triangle():
    triangle = Turtle()
    triangle.right(60)
    triangle.forward(120)
    triangle.right(120)
    triangle.forward(120)
    triangle.right(120)
    triangle.forward(120)
def trapeze():
    trapeze=Turtle()
    trapeze.forward(60)
    trapeze.right(45)
    trapeze.forward(45)
    trapeze.right(135)
    trapeze.forward(90)
    trapeze.right(90)
    trapeze.forward(33)
    
def polygone(form):
    if form == "rectangle":
        rectangle()
    elif form == "triangle":
        triangle()
    elif form == "trapeze":
        trapeze()
    else:
        print("veuillez choisir:rectangle,triangle ou trapeze")

polygone("trapeze")
