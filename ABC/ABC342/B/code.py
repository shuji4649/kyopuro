N=int(input())
P=list(map(int,input().split()))
L=[-1 for _ in range(N)]
for i in range(N):
    L[P[i]-1]=i
Q=int(input())
for _ in range(Q):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if L[a]>L[b]:
        print(b+1)
    else:
        print(a+1)