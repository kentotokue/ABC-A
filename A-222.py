'''
Created on 2021/10/09

@author: kentoo
'''


N = str(input())

ans = ""
if len(N) == 1:
    ans = "000" + N 
elif len(N) == 2 :
    ans = "00" + N 
elif len(N) == 3:
    ans = "0" + N 
else:
    ans = N 
print(ans)