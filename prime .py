
class Solution:
    def isPrime (self, N):
        if N==1:
          return 0
            
        else :
            for i in range(2,N):
              if N%i == 0:
                return 0
            return 1  
        

