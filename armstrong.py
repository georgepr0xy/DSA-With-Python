from os import *
from sys import *
from collections import *
from math import *
n =int(input())
orig_no = n
temp=n
count=0
sumofpower=0
while temp != 0:
    count +=1
    temp //=10
    

while n != 0:
     digit= n%10
     sumofpower += pow(digit,count)
     n //=10 

if sumofpower == orig_no:
    print('true')
else:
    print('false')