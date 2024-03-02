N,M=map(int,input().split())
P=[[]for _ in range(N)]
for i in range(M):
    l,d,k,c,A,B=map(int,input().split())
    P[B-1].append([l,d,k,c,A])
ans=[-1 for _ in range(N)]
import sys
sys.setrecursionlimit(10**9)
from collections import deque
def CanTime(l,d,k,t):
    if t<l :
        return -1
    return l+d*min(k-1,((t-l)//d))

q=deque([(N-1,10**19)])
while q:
    now,time=q.popleft()

    
    for l,d,k,c,A in P[now]:
        ct=CanTime(l,d,k,time-c)+c
        if ct==-1:
            continue
        if ans[A-1]<ct-c:
            # print(now,A-1,ct,ct-c)
            q.append((A-1,ct-c))
            ans[A-1]=ct-c

for i in range(N-1):
    print(ans[i] if ans[i]!=-1 else "Unreachable")


