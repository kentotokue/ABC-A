'''
Created on 2022/01/23

@author: kentoo
'''
a,b,c = map(int,input().split())

if a + b == c or a + c == b or c + b == a:
    print("Yes")
else:
    print("No")