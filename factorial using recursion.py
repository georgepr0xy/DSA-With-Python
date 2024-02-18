# n = 5
# fac =1
# for i in range(1,n+1):
#     fac = fac*i
# print(fac)    


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

a =factorial(5)
print(a)

