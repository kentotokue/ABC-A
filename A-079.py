'''
Created on 2022/01/13

@author: kentoo
'''
N = str(input())

if (N[0] == N[1] == N[2]) or (N[1] == N[2] == N[3]):
    print("Yes")
else:
    print("No")
