'''
Created on 2021/12/02

@author: kentoo
'''
N,K = map(int,input().split())

NUM = N//K 
A = N % K 

if A == 0:
    print("0")
else:
    print(abs((NUM+1)-NUM))

