'''
Created on 2021/06/15

@author: kentoo
'''
A,B,C=map(int,input().split())

Q=A**2+B**2
W=C**2

if Q<W:
    print("Yes")
else:
    print("No")