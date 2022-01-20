'''
Created on 2022/01/20

@author: kentoo
'''
A,B = map(str,input().split())

if A == "H":
    if B == "H":
        print("H")
    else:
        print("D")
else:
    if B == "H":
        print("D")
    else:
        print("H")
    