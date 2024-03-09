N=int(input())
A=list(map(int,input().split()))
Q=int(input())
from collections import defaultdict
INF=10**10
plus=defaultdict(lambda :-1)
pops=set()
address=dict()
for i in range(N):
    address[A[i]]=i
for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        x,y=q[1],q[2]

        if address[x]//INF >=1:
            address[y]=address[x]+1
        else:
            address[y]=INF*(address[x]+1)+address[x]+1
        plus[address[y]]=y
    if q[0]==2:
        x=q[1]
        pops.add((x,address[x]))


pp=0
ans=[]
i=0
while i<N+1:
    while True:
        if plus[INF*i+i+pp]>-1:
            
            if (plus[i+pp+INF*i],i+pp+INF*i) not in pops:
                ans.append(plus[i+pp+INF*i])
            pp+=1
        else: break
    pp=0
    if i==N:
        break
    if (A[i],i) not in pops:
        ans.append(A[i])
    i+=1
print(*ans)

