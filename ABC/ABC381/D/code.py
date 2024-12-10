N=int(input())
A=list(map(int,input().split()))
from collections import defaultdict
d=[0]*N

for i in range(N-1):
    if A[i]==A[i+1]:
        d[i]=A[i]
ans=0
lastUsed=defaultdict(lambda:-3)
start=-2
for i in range(0,N-1,2):
    if d[i]==0:
        start=i
        continue
    if lastUsed[d[i]]<=start:
        lastUsed[d[i]]=i
    else:
        lastUsed[d[i]]=i
        start=lastUsed[d[i]]    
    ans=max(ans,i-start)
lastUsed=defaultdict(lambda:-3)
start=-1
for i in range(1,N-1,2):
    if d[i]==0:
        start=i
        continue
    if lastUsed[d[i]]<=start:
        lastUsed[d[i]]=i
    else:
        lastUsed[d[i]]=i
        start=lastUsed[d[i]]    
    ans=max(ans,i-start)
print(ans)
