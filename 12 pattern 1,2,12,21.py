n= 7
for i in range(1,n):
    for j in range(1,i):
        print(j,end= " ")
    for k in range(n+n-2*i):
        print(" ", end = " ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()            