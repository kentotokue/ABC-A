'''
Created on 2021/08/13

@author: kentoo
'''
K=int(input())
A,B=map(int,input().split())


for i in range(1,1000):
    if K*i>=A and K*i<=B:
        print("OK")
        exit()

print("NG")