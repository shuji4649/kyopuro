
N,H,W=map(int, input().split())
Tiles=[list(map(int, input().split())) for _ in range(N)]
def checkEqual(use):
    sa=0
    for i in use:
        sa+=Tiles[i][0]*Tiles[i][1]
    return sa==H*W
cansolves=[]
for i in range(2**N):
    uses=[]
    for j in range(N):
        if (i>>j)&1:
            uses.append(j)
    if checkEqual(uses):
        cansolves.append(uses)

def dfs(M,uses,n):

    global H,W
    h,w=Tiles[uses[n]]
    for i in range(H-h+1):
        for j in range(W-w+1):
            A=M[:]
            flag=False
            for x in range(i,i+h):
                for y in range(j,j+w):
                    if A[x*w+y]:
                        flag=True
                        break
                    A[x*w+y]=True
                if flag: break

            if not flag:
 
                if len(uses)==n+1:
                    print("Yes")
                    exit()
                dfs(A[:],uses,n+1)
    h,w=w,h
    for i in range(H-h+1):
        for j in range(W-w+1):
            A=M[:]
            flag=False
            for x in range(i,i+h):
                for y in range(j,j+w):
                    if A[x*w+y]:
                        flag=True
                        break
                    A[x*w+y]=True
                if flag: break

            if not flag:
                if len(uses)==n+1:
                    print("Yes")
                    exit()
                dfs(A[:],uses,n+1)
    

for cansolve in cansolves:
    dfs([False for _ in range(H*W)],cansolve,0)
print("No")