import bisect
MOD=998244353
N,K=map(int,input().split())
S=input()
Qpos=[]
for i in range(N):
    if S[i]=="?":
        Qpos.append(i)
dp=[[0 for i in range(8)] for j in range(N+1)] 
for i in range(N):
    if S[i]=="A":
        dp[i+1][4]+=1
        for j in range(8):
            dp[i+1][j^4]+=dp[i][j]
    elif S[i]=="B":
        dp[i+1][2]+=1
        for j in range(8):
            dp[i+1][j^2]+=dp[i][j]
    elif S[i]=="C":
        dp[i+1][1]+=1
        for j in range(8):
            dp[i+1][j^1]+=dp[i][j]
    else:
        dp[i+1][1]+=1
        dp[i+1][2]+=1
        dp[i+1][4]+=1
        for j in range(8):
            dp[i+1][j^1]+=dp[i][j]
            dp[i+1][j^2]+=dp[i][j]
            dp[i+1][j^4]+=dp[i][j]
    dp[i+1][0]+=dp[i+1][7]
    dp[i+1][7]=0

print(dp)

#DPだああああ？？？