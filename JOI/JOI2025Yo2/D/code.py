N,M,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

P=[set() for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    if u>v:
        u,v=v,u
    P[u].add(v)
    P[v].add(u)
X=list(map(int,input().split()))
#################################

newA=[]
for i in range(N):
    newA.append([A[i],i])
newA.sort(reverse=True)
newB=[]
for i in range(N):
    newB.append([B[i],i])
newB.sort(reverse=True)
nowA=0
nowB=0
AnsList=[]
while nowA<N and nowB<N:
    if not (newA[nowA][1]==newB[nowB][1] or (newB[nowB][1] in P[newA[nowA][1]])):
        AnsList.append(newA[nowA][0]+newB[nowB][0])
    if nowA+1>=N:
        nowB+=1
        continue
    if nowB+1>=N:
        nowA+=1
        continue
    else:
        if newA[nowA+1][0]>newB[nowB+1][0]:
            nowA+=1
        else:
            nowB+=1
        continue
for i in range(Q):
    print(AnsList[X[i]-1])