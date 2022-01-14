'''
Created on 2022/01/14

@author: kentoo
'''
C1 = str(input())
C2 = str(input())

C3 = C1[::-1]
if C2 == C3 :
    print("YES")
else:
    print("NO")
'''
if C1[1] == C2[1] and C1[0] == C2[2] and C2[0] == C1[2]:
    print("YES")
else:
    print("NO")
'''