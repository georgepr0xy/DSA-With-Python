target = 5
num=[5,3,1,3,2]
ans=[]
for i in range(len(num)):
    for j in range(len(num)):
        if i == j :
          break
        elif num[i]+num[j] == target:
           ans.append(i)
           ans.append(j)
    j+=1
i+=1           


print(ans)           