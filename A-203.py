'''
Created on 2021/06/14

@author: kentoo
'''
a,b,c=map(int,input().split())

if (a==b):
     print(c)
elif(a==c):
    print(b)
elif(b==c):
    print(a)
else:
    print("0")