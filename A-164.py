'''
Created on 2021/08/13

@author: kentoo
'''
S,W=map(int,input().split())

if S<=W:
    print("unsafe")
else:
    print("safe")