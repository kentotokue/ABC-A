'''
Created on 2021/08/19

@author: kentoo
'''
S=str(input())
A=set(S)
cnt=0
for i in range(len(S)):
    for j in range(i):
        if S[i]==S[j]:
            cnt+=1
        

if len(A)==2 and cnt==2:
    print("Yes")
else:
    print("No")