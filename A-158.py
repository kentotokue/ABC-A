'''
Created on 2021/08/14

@author: kentoo
'''
S=str(input())

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        print("Yes")
        exit()
print("No")
    