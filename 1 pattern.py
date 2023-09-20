n = int(input("Enter the no. of row:"))
for i in range(n):
    for j in range(n):
        print("*", end  = " ")
    print()      


def pattern(n):
    for i in range(n):
       for j in range(n):
         print("*", end  = " ")
       print()   


pattern(5)          
    