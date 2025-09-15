
p=5


for i in range(p,0,-1):
    for space in range(i-1):
        print(" ",end=" ")
    for j in range(i,p+1):
        print(j,end=" ")
    print()  