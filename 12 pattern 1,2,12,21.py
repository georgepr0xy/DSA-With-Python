n= 7
for i in range(1,n):
    for j in range(1,i):
        print(j,end= " ")
    for k in range(2*n-2*i):
        print(" ", end = " ")
    for l in range(1,i):
        print(l,end=" ")
    print()            