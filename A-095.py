'''
Created on 2021/12/15

@author: kentoo
'''
S = str(input())
sum = 700
cnt = 0
for i in range(3):
    if S[i] == "o":
        cnt += 1

print(sum + cnt*100)