'''
Created on 2021/12/09

@author: kentoo
'''
S = str(input())
ans = 0
for i in range(4):
    if S[i] == "+":
        ans += 1
    else:
        ans -= 1

print(ans)