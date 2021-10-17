'''
Created on 2021/09/26

@author: kentoo
'''

A,B,C = map(int,input().split())


for i in range(A,B+1):
    
    if i%C == 0:
        print(i)
        exit()
print("-1")
'''切り上げ計算'''
print((A+(C-1))//C)