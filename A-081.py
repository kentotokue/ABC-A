'''
Created on 2022/01/13

@author: kentoo
'''
S = str(input())

cnt = 0

for i in range(len(S)):
    if S[i] == "1":
        cnt += 1
print(cnt)