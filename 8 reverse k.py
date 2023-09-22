n=5
for i in range(n):
    for j in range(i):
      print(" ",end = " ")
    for k in range(n+4-2*i):
       print("*",end=" ")
    print()   
           