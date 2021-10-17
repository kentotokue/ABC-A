'''
Created on 2021/08/13

@author: kentoo
'''

def swap(a,b):
    
    tmp=0
    tmp=a 
    a=b 
    b=tmp 
    return a,b
X,Y,Z=map(int,input().split())

X,Y=swap(X,Y)
X,Z=swap(X,Z)
print(f"{X} {Y} {Z}")

'''
tmp=0
tmp=A 
A=B 
B=tmp 

tmp=A 
A=C 
C=tmp 

'''