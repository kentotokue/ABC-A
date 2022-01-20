'''
Created on 2022/01/19

@author: kentoo
'''
A,B,C = map(int,input().split())

if A <= C and C <= B:
    print("Yes")
else:
    print("No")