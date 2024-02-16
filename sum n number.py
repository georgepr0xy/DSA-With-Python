# def sumN(N):
#     sum = 0
#     for i in range(N+1):
#         sum = sum + i
#     print(sum)    


# a = sumN(5)

# def sumn(n):
#     sum = int(n*(n+1)/2)
#     print(sum)

# b = sumn(5)

# def sumN(n, sum):
#     if n<1:
#        print(sum)
#        return
    
#     sumN(n-1,sum+n)

# a  = sumN(5,0)
# print(a)        

def sumN(n):
    if n==0:
        return 0
    return n+sumN(n-1)

b = sumN(5)
print(b)    








    