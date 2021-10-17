'''
Created on 2021/08/14

@author: kentoo
'''
N,M=map(int,input().split())

ANS=[2]*N+[1]*M 

cnt=0

for i in range(len(ANS)):
    for j in range(i,len(ANS)):
        if i==j:
            continue
        if (ANS[i]+ANS[j])%2==0:
            cnt+=1

print(cnt)
