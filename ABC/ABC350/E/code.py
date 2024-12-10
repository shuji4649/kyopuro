def isWin(Arr):
    hb=0
    wb=0
    x1=0
    x2=0
    for i in range(3):
        for j in range(3):
            hb+=Arr[i][j]
            wb+=Arr[j][i]
        x1+=Arr[i][i]
        x2+=Arr[i][2-i]
    if hb==3 or wb==3 or x1==3 or x2==3:
        return "Takahashi"
    if hb==-3 or wb==-3 or x1==-3 or x2==-3:
        return "Aoki"
    return "Draw"

A=[list(map(int, input().split())) for i in range(3)]
import sys
sys.setrecursionlimit(10**9)
def dfs(bA,count):
    iswin=isWin(bA)
    if iswin== "Takahashi":
        return (1,0)
    if iswin== "Aoki":
        return (0,1)
    if count==10:
        takapoint=0
        aokipoint=0
        for i in range(3):
            for j in range(3):
                if bA[i][j]==1:
                    takapoint+=A[i][j]
                if bA[i][j]==-1:
                    aokipoint+=A[i][j]
        if takapoint>aokipoint:
            return (1,0)
        else:
            return (0,1)
    pp=0
    tt=0
    aa=0
    for i in range(3):
        for j in range(3):
            if bA[i][j]!=0:
                continue
            bbA=[bA[k][:] for k in range(3)]
            bbA[i][j]=1 if count%2==1 else -1
            t,a=dfs(bbA,count+1)
            pp+=t+a*-1
            tt=max(tt,t)
            aa=max(aa,a)
    
    pp_r=0
    if pp==10-count:
        pp_r=1
    elif pp==-10+count:
        pp_r= -1
    else:
        pp_r= 0

    if count%2==1:
        return (tt,1 if pp_r==-1 else 0)
    else:
        return (1 if pp_r==1 else 0,aa)

t,a=dfs([[0]*3 for i in range(3)],1)
if t==1:
    print("Takahashi")
elif a==1:
    print("Aoki")



