'''
Created on 2021/06/26

@author: kentoo
'''

A,B,C=map(int,input().split())

X=A+B
Y=B+C 
Z=A+C 

print(max(X,Y,Z))
