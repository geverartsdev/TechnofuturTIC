def interet(x):
    if x/10>=15 and x/10<=500:
        x=x+x/10
        return x
    elif x/10<15:
        x=x+15
        return x
    elif x/10>500:
        x=x+500
        return x
print(interet(65))