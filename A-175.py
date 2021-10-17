'''
Created on 2021/08/12

@author: kentoo
'''
S=str(input())
cnt=0

if "RRR"==S:
    cnt=3
elif "RRS"==S or "SRR"==S:
    cnt=2
elif "RSR"==S or "SRS"==S or "SSR"==S or "RSS"==S:
    
    cnt=1
else:
    cnt=0
print(cnt)