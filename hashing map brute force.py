arr= [1,2,1,3,2]
query= [1,3,4,2,10]

for i in range(len(query)):
    count =0
    for j in range(len(arr)):
        if query[i]== arr[j]:
            count +=1
    print(count)      
print()      