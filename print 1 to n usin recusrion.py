count = 0
def fun(N):
    global count
    if count > N:
        return 
    print(count)
    count +=1
    fun(N)


A = fun(5)

