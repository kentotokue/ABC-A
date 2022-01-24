'''
Created on 2022/01/24

@author: kentoo
'''
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(X*N)
else:
    print((X*K)+(Y*(N-K)))