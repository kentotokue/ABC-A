'''
Created on 2021/12/11

@author: kentoo
'''
a,b,c,d = map(int,input().split())

if abs(c - a )<= d :
    print("Yes")
elif (abs(b - a) <= d) and (abs(c - b) <= d):
    print("Yes")
else:
    print("No")