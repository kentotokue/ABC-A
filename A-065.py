'''
Created on 2022/01/18

@author: kentoo
'''
X,A,B = map(int,input().split())

if B - A <= 0 :
    print("delicious")
elif B - A <=  X :
    print("safe")
else:
    print("dangerous")