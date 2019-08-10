number= int(input("entrez votre nombre"))
x=50
min=0
max=100
def plus_moins(number,min,max,x):
    print(x)
    if x==number:
        print("victoire")
    elif rep=="+" :
        min=x+1
        x=min+(max-min)//2
        plus_moins(number,min,max,x)
    elif rep=="-":
        max=x-1
        x=min+(max-min)//2
        plus_moins(number,min,max,x)
    print(x)
plus_moins( number,min,max,x)