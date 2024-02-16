def sumofn(N,sum):
    if N<1:
        print(sum)
    sumofn(N-1,sum+1 )

a=sumofn(5,0)  
print(sum)  

