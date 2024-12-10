MOD=998244353
N,M,K=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
S=[[list(map(int,input().split())) for _ in range(3)]for _ in range(M)]
ansL=0
anses=[]
for i in range(K):
    maxnum=-1
    maxm=0
    maxpos=(0,0)
    for m in range(M):
        for x in range(N-3):
            for y in range(N-3):
                plus=0
                for xxx in range(3):
                    for yyy in range(3):
                        plus+=(A[x+xxx][y+yyy]+S[m][xxx][yyy])%MOD-A[x+xxx][y+yyy]
                if plus>maxnum:
                    maxnum=plus
                    maxm=m
                    maxpos=(x,y)
    if maxnum<=0:
        break
    ansL+=1
    for xxx in range(3):
        for yyy in range(3):
            A[maxpos[0]+xxx][maxpos[1]+yyy]=(A[maxpos[0]+xxx][maxpos[1]+yyy]+S[maxm][xxx][yyy])%MOD
    anses.append([maxm,*maxpos])
print(ansL)
for a in anses:
    print(*a)

