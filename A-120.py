'''
Created on 2021/09/24

@author: kentoo
'''
A,B,C = map(int,input().split())
if B//A >=C:
    print(C)
else:
    print(B//A)