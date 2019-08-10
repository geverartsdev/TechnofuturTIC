import random

def roll_dice():
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    d3=random.randint(1,6)
    total=d1+d2+d3
    print(total)
    if total==14:
        print("true")
    else:
        print("false")
 
roll_dice()

