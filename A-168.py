'''
Created on 2021/08/13

@author: kentoo
'''
N=str(input())
l=len(N)-1



if int(N[l])==3:
    print("bon")
elif int(N[l])==0 or int(N[l])==1 or int(N[l])==6 or int(N[l])==8:
    print("pon")
else:
    print("hon")