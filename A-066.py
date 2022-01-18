'''
Created on 2022/01/18

@author: kentoo
'''
a,b,c = map(int,input().split())
S1 = a+b 
S2 = a+c 
S3 = b+c 
print(min(S1,S2,S3))