import sys
sys.setrecursionlimit(10**9)

N,X=map(int,input().split())
A=list(map(int,input().split()))
P=list(map(int,input().split()))

Tree=[[] for _ in range(N)]
for i in range(N):
    if P[i]!=-1:
        Tree[P[i]-1].append(i)

ans=-1

def dfs(v,cost):
    global ans
    if cost+A[v]>X:
        return
    ans=max(ans,v+1)
    for i in Tree[v]:
        dfs(i,cost+A[v])
for i in range(N):
    if P[i]>-1:
        continue
    dfs(i,0)
print(ans)
    
