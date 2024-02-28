# def count():
#     arr = list(map(int,input("enter the array:").split(',')))
#     print(arr)
#     # n = len(arr)
#     # newarr = [0] * len(arr)
#     unique = set(arr)
#     for i in unique:
         
#          print(i, end =" ")
#          counting = 0
#          for j in range(len(arr)):
#            if i == arr[j]:
#              counting += 1
#          print(counting)


# count()         

#----------------------------------------------------------------->
#--------using map approach-------------->

arr = [10,5,10,15,10,5]
n = len(arr)

def countfreq(arr,n):
    mp = {}
    for i in range(n):
       if arr[i] in mp:
            mp[arr[i]] += 1
       else: 
            mp[arr[i]] = 1
    for x in mp:
        print(x,mp[x])   

b= countfreq(arr,n)

    
    
           





        












# arr = list(map(int,input("enter the array:").split()))
# print(arr)
    