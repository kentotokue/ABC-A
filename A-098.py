'''
Created on 2021/12/11

@author: kentoo
'''
A,B = map(int,input().split())
ans = max(A+B,A-B,A*B)
print(ans)