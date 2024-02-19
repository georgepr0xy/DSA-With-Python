# str = "ABCDCBA"
# p1 = 1
# p2 = len(str)-1

# while p1<p2:
#   if str[p1] == str[p2]:
#     p1 += 1
#     p2 -= 1

#   elif:
#      print("Its is not a palindrome")
  
s = "madam"
def  palindrome(i,s):
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-1-i]:
        return False
    return palindrome(i+1,s)

b = palindrome(0,s)
print(b)
