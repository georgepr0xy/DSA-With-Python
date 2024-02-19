def fibonacci(n):
    if n == 0:
        print(n)
    elif n == 1:
        print(n)
    else:
        
        fib= [0]* (n+1)
        fib[0] =0
        fib[1] =1

        for i in range(2,n+1):
            fib[i] = fib[i-1]+fib[i-2]
        print(fib)   


b = fibonacci(5)


