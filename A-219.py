'''
Created on 2021/09/18

@author: kentoo
'''
X=int(input())

if 0<=X and X<40:
    print(40-X)
elif 40<=X and X<70:
    print(70-X)
elif 70<=X and X<90:
    print(90-X)
else:
    print("expert")