def count():
    arr = list(map(int,input("enter the array:").split(',')))
    print(arr)
    # n = len(arr)
    # newarr = [0] * len(arr)
    unique = set(arr)
    for i in unique:
         
         print(i, end =" ")
         counting = 0
         for j in range(len(arr)):
           if i == arr[j]:
             counting += 1
         print(counting)


count()         
        












# arr = list(map(int,input("enter the array:").split()))
# print(arr)
    