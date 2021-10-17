'''
Created on 2021/08/29

@author: kentoo
'''

X,Y=map(int,input().split("."))


if 0<=Y and Y<=2:
    print(f"{X}-")
elif 3<=Y and Y<=6:
    print(f"{X}")
else:
    print(f'{X}+')