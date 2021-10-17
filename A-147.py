'''
Created on 2021/08/15

@author: kentoo
'''
A=list(map(int,input().split()))

sum=0

for i in A:
    sum+=i 
    
if sum>=22:
    print("bust")
else:
    print('win')
    