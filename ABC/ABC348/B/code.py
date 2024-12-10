N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]
ans=[0]*N
p=[0]*N
for i in range(N):
    for j in range(N):
        a=(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2
        if p[i]<a:
            p[i]=a
            ans[i]=j
for i in range(N):
    print(ans[i]+1)