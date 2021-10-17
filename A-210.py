'''
Created on 2021/07/17

@author: kentoo
'''
N,A,X,Y=map(int,input().split())

if N>A:
    print(A*X+(N-A)*Y)
else:
    print(N*X)
    