'''
Created on 2021/08/18

@author: kentoo
'''

N=int(input())
cnt=0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            cnt+=1
            

print(cnt)
