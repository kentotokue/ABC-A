'''
Created on 2022/01/14

@author: kentoo
'''
A,B,C = map(int,input().split())

if A == B :
    print(C)
elif A == C:
    print(B)
else:
    print(A)