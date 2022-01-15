'''
Created on 2022/01/15

@author: kentoo
'''
N = str(input())

if N == N[::-1]:
    print("Yes")
else:
    print("No")