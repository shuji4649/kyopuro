S=input()
from collections import defaultdict
D=defaultdict(int)
for s in S:
    D[s]+=1
ans=len(S)*(len(S)-1)//2
flag=0
for k in D.values():
    if k>=2:
        flag=1
    ans-=k*(k-1)//2
print(ans+flag)