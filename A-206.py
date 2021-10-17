'''
Created on 2021/06/19

@author: kentoo
'''
N=int(input())

X=round(1.08*N) 

if X<206:
    print("Yay!")
elif X==206:
    print("so-so")
else:
    print(":(")