'''
Created on 2022/01/19

@author: kentoo
'''

A,B,C = map(str,input().split())

if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")