'''
Created on 2021/06/21

@author: kentoo
'''
def sumn (n):
    ans=0
    while n:
        ans+=n%10
        
        n//=10
    return ans

A,B=map(int,input().split())

a=sumn(A)
b=sumn(B)

if a==b:
    print(a)
else:
    print(max(a,b))
        
        
        