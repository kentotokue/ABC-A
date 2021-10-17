'''
Created on 2021/08/14

@author: kentoo
'''
N,R=map(int,input().split())

if N>=10:
    print(R)
else:
    print(R+(100*(10-N)))