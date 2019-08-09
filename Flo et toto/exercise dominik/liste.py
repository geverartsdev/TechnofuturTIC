t=[1,45,67,34,12,89,45,23,10,43]

def trouve(x):
    for i in range(0,len(t)):
        if x== t[i]:
            return("true")
    return("false")
#print(trouve(45))
def trouve_indice (x):
    ind = -1
    for i in range(0,len(t)):
        if x==t[i]:
            ind = i
    return ind
#print(trouve_indice(45))
def add_tout():
    total=0
    for i in range(0,len(t)):
        total+=t[i]
    return total
#print(add_tout())
def remplace(valeur,indice):
    t[indice] = valeur
    print(t)
    
remplace(101,2)


        

        