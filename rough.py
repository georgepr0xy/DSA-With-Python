# def matrix(m,n):
#     o= []
#     for i in range(m):
#         row =[]
#         for j in range(n):
#             userin = int(input(f"enter o[{i}{j}]"))
#             row.append(userin)

#         o.append(row)        
#     return o

# print("enter the size of matrix MXN\n")
# m= int(input("enter the value of M:\n"))
# n= int(input("enter the value of n:\n"))


# print("matrix A:")
# A = matrix(m,n)
# print(A)


# m = len(A)
# n = len(A[0])

# print(m)
# print(n)


# rev = int(input("enter the string :"))

# rev = str(rev)
# rev =rev[::-1]
# rev= int(rev)
# print(rev)



# num = 1//10
# print(num)
# a=4
# b=8
# r=gcd(a,a%b)

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# if __name__ == "__main__":
#     a = 3
#     b = 7
#     print("The GCD of the two numbers is", gcd(a, b))


# print(3%1)    


# temp = 332
# temp %= 10
# print(temp)

# n= 35
# for i in range(1,n):
#     if n%i==0:
#         print(i,end =' ')
# print()    
# from math import sqrt
# a= sqrt(5)
# b=4
# print(a,b)


# cnt = 0

# def print_function():
#     global cnt

#     # Base Condition.
#     if cnt == 3:
#         return 1
    
#     print(cnt)
    

#     # Count Incremented
#     cnt += 1
#     print_function()

# if __name__ == "__main__":
#     print_function()



# n = 5
# ans = [0] * n
# print(ans)
# n = int(input("enter:"))
# arr = list(map(int, input().split()))
# print(arr)
# def main():
#     # n = int(input())
#     arr = list(map(int, input().split()))

#     # precompute
#     hash_table = [0] * 13
#     for num in arr:
#         hash_table[num] += 1

#     q = int(input())
#     while q > 0:
#         number = int(input())
#         # fetching
#         print(hash_table[number])
#         q -= 1

# if __name__ == "__main__":
#     main()
arr = list(map(int,input("enter the array:").split()))
unique = set(arr)
print(unique)
for i in unique:
    print(i)