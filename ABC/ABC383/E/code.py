N,X,K=map(int,input().split())
Item=[list(map(int,input().split())) for _ in range(N)]
Colors=[[] for _ in range(N)]
for i in range(N):
    Colors[Item[i][2]-1].append(Item[i])

ColorDPed=[[(0,0)] for _ in range(N)]
for i in range(N):
    cDP=[[0 for _ in range(X+1)] for _ in range(len(Colors[i])+1)]
    for j in range(len(Colors[i])):
        for k in range(X+1):
            if k>=Colors[i][j][0]:
                cDP[j+1][k]=max(cDP[j][k-Colors[i][j][0]]+Colors[i][j][1],cDP[j][k])
            else:
                cDP[j+1][k]=cDP[j][k]
    for j in range(X+1):
        if cDP[len(Colors[i])][j]>0:
            cDP[len(Colors[i])][j]+=K
            if cDP[len(Colors[i])][j-1]<cDP[len(Colors[i])][j]:
                ColorDPed[i].append((j,cDP[len(Colors[i])][j]))

dp=[[0 for _ in range(X+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(X+1):
        dp[i+1][j]=max(dp[i][j],dp[i+1][j])
        for k in range(len(ColorDPed[i])):
            if ColorDPed[i][k][0]<=j:
                dp[i+1][j]=max(dp[i][j-ColorDPed[i][k][0]]+ColorDPed[i][k][1],dp[i+1][j])
            else:
                break
print(dp[N][X])