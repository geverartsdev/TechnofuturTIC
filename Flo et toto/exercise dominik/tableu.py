t1=[1,25,7]
t2=[8,91,45]
t3=[61,12,17]
Mat=[t1,t2,t3]

def matrice (Mat):
    print(Mat)
matrice(Mat)
def mat2(Mat):
    for i in range (0,len(t1)):
        print(t1[i])
    for i in range (0,len(t2)):
        print(t2[i])
    for i in range (0,len(t3)):
        print(t3[i])
        
#mat2(Mat)
def mat2_2(Mat):
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            print(Mat[i][j])
            
        
#mat2_2(Mat)