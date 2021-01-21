from collections import defaultdict
import heapq
n=int(input())
m=int(input())
G=defaultdict(list)
INF=9999999
for _ in range(m):
    a,b,c=map(int,input().split(' '))
    G[a].append((b,c))


def dijkstra(start,cost,visited):
    visited[start]=0
    queue=[]
    heapq.heappush(queue,(cost,start))
    while queue:
        distance,node=heapq.heappop(queue)
        if distance > visited[node]:
            continue
        for i in G[node]:
            cost=i[1]+distance
            if cost < visited[i[0]]:
                visited[i[0]]=cost
                heapq.heappush(queue,(cost,i[0]))
    return visited
result=[]
for start in range(1,n+1):
    result.append(dijkstra(start,0,[INF]*(n+1))[1:])
for i in result:
    for j in i:
        if j==INF:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()

'''
플로이드 와샬

점화식을 이용하여 각각의 지점에서 인접리스트로 표현된 Graph를 통하여 풀수도있음.
ex) graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

'''
