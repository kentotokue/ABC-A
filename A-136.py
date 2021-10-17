'''
Created on 2021/08/18

@author: kentoo
'''
A,B,C=map(int,input().split())

ans=C-(A-B)

if ans>0:
    print(ans)
else:
    print("0")