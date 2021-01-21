n=int(input())
p=list(map(int,input().split(' ')))
p.sort()
wait=0
summ=0
for t in p:
    time = t + wait
    wait = time
    summ+=time
print(summ)
