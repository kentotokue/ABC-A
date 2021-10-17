'''
Created on 2021/08/27

@author: kentoo
'''
A,B = map(int,input().split())
sum=0
for i in range(2):
    sum+=max(A,B)
    if A==max(A,B):
        A-=1
    else:
        B-=1 

print(sum)