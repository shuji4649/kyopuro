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

if Q==1 and X[0]==1:
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

    while nowA<N and nowB<N:
        if newA[nowA][1]==newB[nowB][1] or (newB[nowB][1] in P[newA[nowA][1]]):
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
        else:
            print(newA[nowA][0]+newB[nowB][0])
            exit()

if N<=50 and M<=50 and Q<=50:
    ANS=[]
    for i in range(N):
        for j in range(i+1,N):
            if j in P[i]:
                continue
            ANS.append([max(A[i],A[j])+max(B[i],B[j]),i,j])
    ANS.sort(reverse=True)
    for i in range(Q):
        print(ANS[X[i]-1][0])
    exit()

small4Flag=True
for i in range(N):
    if B[i]!=1:
        small4Flag=False
        break
if small4Flag:
    newA=[]
    for i in range(N):
        newA.append([A[i],i])
    newA.sort(reverse=True)
    NoCount=[0]*N
    before=set()
    for i in range(N):
        before.add(newA[i][1])
        for j in P[newA[i][1]]:
            if j not in before:
                NoCount[i]+=1  
    Anses=[]
    for i in range(N):
        num=N-1-i-NoCount[i]
        if len(Anses)>0 and Anses[-1][0]==newA[i][0]:
            Anses[-1][1]+=num
        else:
            Anses.append([newA[i][0],num])

    sumAnses=[0]
    for i in range(len(Anses)):
        sumAnses.append(sumAnses[-1]+Anses[i][1])

    import bisect
    for i in range(Q):
        index=bisect.bisect_left(sumAnses,X[i])
        print(Anses[index-1][0]+1)
