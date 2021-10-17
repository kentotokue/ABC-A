'''
Created on 2021/08/13

@author: kentoo
'''
N=str(input())

for i in range(len(N)):
    if N[i]=="7":
        print("Yes")
        exit()

print("No")