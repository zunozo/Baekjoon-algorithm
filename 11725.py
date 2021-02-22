from collections import deque

n=int(input())
G=[[] for _ in range(n+1)]
visited=[False]*(n+1)
Parent={}

for _ in range(n-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)



def bfs():
    queue=deque([1])
    visited[1]=True
    while queue:
        node=queue.popleft()
        for i in G[node]:
            if not visited[i]: #방문하지않았다면
                Parent[i]=node
                queue.append(i)
                visited[i]=True
bfs()

for i in range(2,n+1):
    print(Parent[i])
