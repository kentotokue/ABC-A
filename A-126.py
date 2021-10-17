'''
Created on 2021/08/23

@author: kentoo
'''
N,K=map(int,input().split())
S=str(input())

A=S.replace(S[K-1],S[K-1].lower())
print(A)