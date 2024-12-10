H,W,Q=map(int,input().split())
Ans=[[0]*W for _ in range(H)]
for _ in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        x,y,c=q[1]-1,q[2]-1,q[3]
        for i in range(2):
            for j in range(2):
                if 0<=x+i<H and 0<=y+j<W and Ans[x+i][y+j]>=0:
                    Ans[x+i][y+j]=c 
    if q[0]==2:
        x,y=q[1]-1,q[2]-1
        for i in range(2):
            for j in range(2):
                if 0<=x+i<H and 0<=y+j<W:
                    if Ans[x+i][y+j]>=0:
                        Ans[x+i][y+j]=-Ans[x+i][y+j]-1

for i in range(H):
    ans=[]
    for j in range(W):
        if Ans[i][j]>=0:
            ans.append(Ans[i][j])
        else:
            ans.append(-Ans[i][j]-1)
    print(*ans)