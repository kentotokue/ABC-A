'''
Created on 2022/01/19

@author: kentoo
'''
x,y = map(int,input().split())

L1 = [1,3,5,7,8,10,12]
L2 = [4,6,9,11]
L3 = 2

if x in L1 and y in L1:
    print("Yes")
elif x in L2  and y in L2 :
    print("Yes")
elif x == 2 and y == 2:
    print("Yes")
else:
    print("No")