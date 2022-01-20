'''
Created on 2022/01/20

@author: kentoo
'''
A,B = map(int,input().split())

sum = A + B 
if sum <= 23:
    print(sum)
else:
    print(sum-24)