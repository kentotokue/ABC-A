'''
Created on 2021/06/21

@author: kentoo
'''
X,Y=map(int,input().split())

if (abs(X-Y)<3):
    print("Yes")
else:
    print("No")