def matrix(m,n):
    o= []
    for i in range(m):
        row =[]
        for j in range(n):
            userin = int(input(f"enter o[{i}{j}]"))
            row.append(userin)

        o.append(row)        
    return o


def sum(A,B):
    result=[]
    for i in range(len(A)):
        rowsum=[]
        for j in range(len(B)):
            sum = A[i][j]+B[i][j]
            rowsum.append(sum)    
        result.append(rowsum)   
    return(result)     

print("enter the size of matrix MXN\n")
m= int(input("enter the value of M:\n"))
n= int(input("enter the value of n:\n"))

print("matrix A:")
A = matrix(m,n)
print(A)

print("matrix B")
B= matrix(m,n)
print(B)


s= sum(A,B)
print("the sum of matrix A and B is :", s)

