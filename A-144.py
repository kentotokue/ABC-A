'''
Created on 2021/08/17

@author: kentoo
'''
A,B=map(int,input().split())

if (A<=9 and A>=1) and (B>=1 and B<=9):
    print(A*B)
else:
    print("-1")
    
