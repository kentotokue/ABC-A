'''
Created on 2022/01/15

@author: kentoo
'''
X,A,B = map(int,input().split())

if abs(X-A) > abs(X-B):
    print("B")
else:
    print("A")