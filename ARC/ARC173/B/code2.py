from collections import defaultdict
N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]
import math
def line(p1,p2):
    x1,y1=p1
    x2,y2=p2
    a=y2-y1
    b=-1*(x2-x1)
    c=-b*y1-a*x1
    g=math.gcd(a,math.gcd(b,c))
    if g!=0:
        a,b,c=a//g,b//g,c//g
    if(a<0):
        a,b,c=-a,-b,-c
    return (a,b,c)
ts=set()
D=defaultdict(int)
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if line(P[i],P[j])!=line(P[j],P[k]):
                ts.add((i,j,k))
                D[i]+=1
                D[j]+=1
                D[k]+=1
ans=0
so_T=list(sorted(ts,key=lambda x:D[x[0]]+D[x[1]]+D[x[2]]))
used=set()
for i in so_T:
    for j in i:
        if j in used:
            break
    else:
        ans+=1
        used|=set(i)
print(ans)