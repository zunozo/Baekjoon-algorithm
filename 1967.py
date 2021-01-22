import sys
sys.setrecursionlimit(10**8)

from collections import defaultdict
n=int(input())
G=defaultdict(list)
for _ in range(n-1):
    a,b,dis=map(int,input().split(' '))
    G[a].append((b,dis))
    G[b].append((a,dis))
maxi,start=0,0
def dfs(node,dist,visited):
    global maxi,start
    visited[node]=1
    if all(visited[x[0]] for x in G[node]):
        if maxi < dist:
            
            maxi,start=dist,node
            return
    for n,cost in G[node]:
        if visited[n]==0: #방문x
            dfs(n,dist+cost,visited)           
dfs(1,0,[0]*(n+1))
maxi=0
dfs(start,0,[0]*(n+1))
print(maxi)
'''
dfs,bfs
'''
