'''
Created on 2021/08/18

@author: kentoo
'''
S=str(input())

D=["Sunny","Cloudy", "Rainy","Sunny"]

for i in range(4):
    if D[i]==S:
        print(D[i+1])
        exit()