'''
Created on 2021/08/14

@author: kentoo
'''
N=int(input())

page=N//2

if N%2==0:
    print(page)
else:
    print(page+1)