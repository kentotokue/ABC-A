'''
Created on 2021/08/18

@author: kentoo
'''

N=int(input())

if N%2==0:
    print((N/2)/N)
else:
    print(((N//2)+1)/N)