def get_parent(x):
    if x==node[x]:
        return x
    node[x]=get_parent(node[x])
    return node[x]

    
def union_parent(x,y):
    x=get_parent(x)
    y=get_parent(y)

    if x!=y:
        node[x]=y
        count[y]+=count[x]
        
        
t=int(input())
for _ in range(t):
    node={}
    count={}
    f=int(input())
    for _ in range(f):
        a,b=input().split()
        if a not in node:
            node[a]=a
            count[a]=1
        if b not in node:
            node[b]=b
            count[b]=1
        union_parent(a,b)
        print(count[get_parent(b)])
