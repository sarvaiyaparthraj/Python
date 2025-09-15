p=5;


for d in range(p,0,-1):
    for space in range(d-1):
        print(" ",end=" ")
    for j in range(p-d+1):
        print(d, end=" ")
    print()        