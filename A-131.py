'''
Created on 2021/08/20

@author: kentoo
'''
S=str(input())

for i in range(len(S)-1):
    if S[i]==S[i+1]:
        print("Bad")
        exit()
print("Good")