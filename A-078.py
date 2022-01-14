'''
Created on 2022/01/14

@author: kentoo
'''
X,Y = map(str,input().split())

if X > Y:
    print(">")
elif X == Y:
    print("=")
else:
    print("<")