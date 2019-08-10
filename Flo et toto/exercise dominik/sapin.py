def sapin ():
    y=int(input("taille du sapin ?"))
    for x in range (1,(y+1)):
        print(" "*(y-x)+"^ "*x)
sapin()
