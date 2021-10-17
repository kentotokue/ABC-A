'''
Created on 2021/07/17

@author: kentoo
'''
N,X,T=map(int,input().split())

A=N//X 
a=N%X 

if a==0:
    print(A*T)
else:
    print((A+1)*T)