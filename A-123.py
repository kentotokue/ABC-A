'''
Created on 2021/08/27

@author: kentoo
'''
A = []
for i in range(6):
    A.append(int(input()))
flag = True

for i in range(4):
    for j in range(i,4):
        if i==j:
            continue
        #print(i,j)
        #print(A[j]-A[i])
        if A[j]-A[i]>A[5]:
            flag = False
            
    

if flag:
    
    print("Yay!")
else:
    print(":(")
