from collections import defaultdict
N=int(input())
D=defaultdict(set)
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

for i in range(N):
    for j in range(i+1,N):
        D[line(P[i],P[j])]|={i,j}
for i in D.values():
    if len(i)>=N-N//3+1:
        print(N-len(i))
        exit()
print(N//3)
