import math

n=int(input())
A=list(map(int,input().split()))
b,c=map(int,input().split())

mini=n

for num in A:
    if num-b<=0:
        continue
    mini+=math.ceil((num-b)/c)
print(mini)
        
'''
구현?
'''
