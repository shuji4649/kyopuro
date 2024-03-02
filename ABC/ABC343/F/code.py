N=int(input())
A=list(map(int,input().split()))
Q=int(input())
Qs=[]
for _ in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        Qs.append([*q[1:],True])
    elif q[0]==2:
        Qs[q[1]-1][3]=False
    else:
        a=q[1]-1
        ans=0
        for l,r,x,f in Qs:
            if l<=a<=r and f:
                ans=max(ans,x)
        print(ans)
