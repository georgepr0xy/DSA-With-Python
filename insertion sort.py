def sort(nums):
    for i in range(5):
     minpos=i
     for j in range(i,6):
       if nums[j]<nums[minpos]:
         minpos = j

         temp = nums[i]
         nums[i]= nums[minpos]
         nums[minpos]=temp

nums=[3,2,7,4,9,1]         
sort(nums)
print(nums)