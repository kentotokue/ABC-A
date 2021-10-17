'''
Created on 2021/08/13

@author: kentoo
'''
X=list(map(int,input().split()))

cnt=0

for i in X:
    if i==0:
        cnt=X.index(i)

print(cnt+1)