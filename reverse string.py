arr = [5,4,3,2,1]
n = len(arr)
# for i in range(n-1,-1,-1):
#     print(i, end='')


def printarr(arr,n):
    for i in range(n):
        print( arr[i], end = ",")
      

def revstring(arr,n):
    p1 = 0
    p2 = n-1
    
    while p1<p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    printarr(arr,n)   

rev = revstring(arr,n)
        


