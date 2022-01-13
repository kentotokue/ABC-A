'''
Created on 2021/11/27

@author: kentoo
'''
N = list(map(int,input().split()))
N.sort(reverse = True)


print(N[0]*10+N[1]+N[2])
