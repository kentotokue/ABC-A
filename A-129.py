'''
Created on 2021/08/21

@author: kentoo
'''
P,Q,R=map(int,input().split())

sum=P+Q+R 

print(min(sum-P,sum-Q,sum-R))