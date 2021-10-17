'''
Created on 2021/07/31

@author: kentoo
'''
A,B=map(int,input().split())

if 0<A and B==0:
    print("Gold")
elif A==0 and 0<B:
    print("Silver")
else:
    print("Alloy")