'''
Created on 2022/01/23

@author: kentoo
'''
A,B = map(int,input().split())

if A == 1 and B == 1:
    print("Draw") 
elif A == 1 :
    print("Alice")
elif B == 1 :
    print("Bob")
elif A == B :
    print("Draw")
elif A < B :
    print("Bob")
else:
    print("Alice")
    