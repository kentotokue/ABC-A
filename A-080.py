'''
Created on 2022/01/13

@author: kentoo
'''
N,A,B = map(int,input().split())

if A*N > B :
    print(B)
else:
    print(A*N)