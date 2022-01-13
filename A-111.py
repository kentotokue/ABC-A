'''
Created on 2021/11/27

@author: kentoo
'''

N = str(input())
ans = []
for i in range(3):
    if N[i] == "1":
        ans.append("9")
    else:
        ans.append("1")
A = "".join(ans)
print(A)
    