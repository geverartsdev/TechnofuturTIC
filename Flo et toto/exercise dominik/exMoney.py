def rendreMonnaie(x):
    B20=x//20
    r20=x%20
    B10=(r20)//10
    r10=r20%10
    B5=(r10)//5
    r5=r10%5
    P2=(r5)//2
    r2=r5%2
    P1=(r2)//1
    return B20,B10,B5,P2,P1
print(rendreMonnaie(197))
