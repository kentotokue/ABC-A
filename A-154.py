'''
Created on 2021/08/14

@author: kentoo
'''
S,T=map(str,input().split())
A,B=map(int,input().split())

U=str(input())

if S==U:
    print(f"{A-1} {B}")
else:
    print(f"{A} {B-1}")