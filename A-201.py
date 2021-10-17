'''
Created on 2021/06/14

@author: kentoo
'''
'''
a,b,c=map(int,input().split())

if b-a==a-c:
    print("Yes")
elif a-b==b-c:
    print("Yes")
elif a-c==c-b:
    print("Yes")
elif c-a==a-b:
    print("Yes")
elif c-b==b-a:
    print("Yes")
elif b-c==c-a:
    print("Yes")
    
else:
    print("No")
'''

A=list(map(int,input().split()))

A.sort()

ans="no"

if A[0]-A[1]==A[1]-A[2]:
    ans="Yes"
    
print(ans)