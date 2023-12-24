n= int(input("enter the vlaue of lenth of row:"))

for i in range(n):
    
    for j in range(n-i):
        print(" ", end ="")
    
    for k in range(i):
        print(f"{k+1}",end=" ")

    print()    
