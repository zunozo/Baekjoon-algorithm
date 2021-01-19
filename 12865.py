N,K = map(int,input().split())

W = [0 for x in range (N+1)]
V = [0 for x in range (N+1)]
DP = [[0 for x in range(K+1)] for x in range (N+1)]
for x in range (1,N+1) :
    W[x],V[x] = map(int,input().split())

for i in range (1,N+1) :
    for j in range (1,K+1) :
        if j >= W[i] : # 아직 넣을수 있다면,
            DP[i][j] = max(V[i]+DP[i-1][j-W[i]],DP[i-1][j])  # 넣는것과 안넣는것 중 최대값을 가져옴.
        else :
            DP[i][j] = DP[i-1][j]
print(DP[-1][-1])
