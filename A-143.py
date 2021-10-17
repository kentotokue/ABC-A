'''
Created on 2021/08/17

@author: kentoo
'''
A,B=map(int,input().split())

ans=A-2*B 

if ans>0:
    print(ans)
else:
    print("0")