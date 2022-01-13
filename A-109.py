'''
Created on 2021/11/28

@author: kentoo
'''
A,B = map(int,input().split())

sum = A * B 

if sum % 2 == 0:
    print("No")
else:
    print("Yes")