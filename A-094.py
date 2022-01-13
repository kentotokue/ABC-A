'''
Created on 2021/12/16

@author: kentoo
'''
A,B,X = map(int,input().split())

if( A > X ) or ((A+B)<X):
    print("NO")
else:
    print("YES")