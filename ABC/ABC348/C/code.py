N=int(input())
from collections import defaultdict
d=defaultdict(lambda: 10**10)
for i in range(N):
    a,c=map(int,input().split())
    d[c]=min(d[c],a)
ans=0
for i in d.values():
    ans=max(ans,i)
print(ans)