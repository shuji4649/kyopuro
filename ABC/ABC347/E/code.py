N,Q=map(int,input().split())
X=list(map(int,input().split()))
from collections import defaultdict
d=defaultdict(list)
dl=defaultdict(int)
S=[0]
for i in range(Q):
    x=X[i]-1
    d[x].append(i)
    if dl[x]%2==0:
        S.append(S[-1]+1)
    else:
        S.append(S[-1]-1)
    dl[x]+=1
ans=[]
Ssum=[0]
for i in range(len(S)-1):
    Ssum.append(Ssum[-1]+S[i+1])
for i in range(N):
    a=0
    if len(d[i])%2==1:
        d[i].append(Q)
    for j in range(0,len(d[i]),2):
        a+=Ssum[d[i][j+1]]-Ssum[d[i][j]]
    ans.append(a)
print(*ans)
    
