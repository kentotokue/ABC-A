'''
Created on 2021/08/21

@author: kentoo
'''
A,B=map(int,input().split())

if A>=13:
    print(B)
elif 6<=A and A<=12:
    print(B//2)
else:
    print("0")