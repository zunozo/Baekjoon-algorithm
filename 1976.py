import sys
sys.setrecursionlimit=10**8

n=int(input())
m=int(input())
G=[]
for _ in range(n):
    k=list(map(int,input().split()))
    G.append(k)
m=list(map(int,input().split()))
K=[]
for i in range(len(G)):
    for j in range(i+1,len(G[i])):
        if G[i][j]:
            K.append((i,j))
parent=[i for i in range(n)]
def get_parent(x):
    global parent
    if parent[x] == x:
        return x
    parent[x]=get_parent(parent[x])
    return parent[x]
def union_parent(i,j):
    global parent
    i=get_parent(i)
    j=get_parent(j)
    if i<j:
        parent[j]=i
    else:
        parent[i]=j
for i,j in K:
    union_parent(i,j)
if len(m)>1:
    key=parent[m[0]-1]
    for i in m[1:]:
         if key!=parent[i-1]:
             print('NO')
             break
    else:
        print('YES')

'''unionfind'''
