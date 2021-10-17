'''
Created on 2021/06/15

@author: kentoo
'''
N=int(input())

if(1<=N and N<=100):
    print("1")
else:
    if N%100==0:
        print(N//100)
    else:
        Y=N//100+1
        print(Y)
        
 
