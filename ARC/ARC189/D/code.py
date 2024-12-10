N=int(input())
A=list(map(int,input().split()))
P=[]
for i in range(N):
    P.append([A[i],i])
P.sort()
ans=[0 for i in range(N)]
for i in range(N):
    x,j=P[i]
    if j==0:
        if A[1]<x:
            ans[j]=x+A[1]