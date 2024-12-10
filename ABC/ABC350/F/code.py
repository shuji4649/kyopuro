N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
from collections import defaultdict
P=[defaultdict(set) for _ in range(M)]
for i in range(N):
    for j in range(M):
        P[j][A[i][j]].add(i)
tmp=[0]*(N*N)
for d in P:
    for i in d.values():
        for j in i:
            for k in i:
                if j<k:
                    tmp[j*N+k]+=1
ans=0
for i in tmp:
    if i%2==1:
        ans+=1
print(ans)
