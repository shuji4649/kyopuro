T=input()
N=int(input())
INF=10**18
dp=[[INF for _ in range(len(T)+1)] for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
    S=list(input().split())[1:]
    for j in range(len(T)+1):
        dp[i+1][j]=dp[i][j]
    for j in range(len(T)+1):
        for k in S:
            if j-len(k)<0:
                continue

            if T[j-len(k):j]==k:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j-len(k)]+1)

if dp[N][len(T)]!=INF:
    print(dp[N][len(T)])
else:
    print("-1")
