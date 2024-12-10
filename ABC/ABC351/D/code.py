H,W=map(int,input().split())
S=[input() for i in range(H)]
import sys
sys.setrecursionlimit(10**9)
memo={}
import pypyjit 
pypyjit.set_param('max_unroll_recursion=-1')
def dfs(x,y,lv):
    #print(x,y,visited)
    visited=set()
    visited.add((x,y))
    lv.add((x,y))
    flag=False
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx,ny=x+dx,y+dy
        if 0<=nx<H and 0<=ny<W and S[nx][ny]=="#":
            flag=True
            break
    if flag:
        #print("b",x,y,visited)
        memo[(x,y)]=visited
        return visited
    else:
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny=x+dx,y+dy
            if 0<=nx<H and 0<=ny<W and ((nx,ny) not in lv):
                if (nx,ny) in memo.keys():
                    visited|=(memo[(nx,ny)])
                else:
                    visited|=dfs(nx,ny,lv.copy())
        #print("a",x,y,visited)
        memo[(nx,ny)]=visited
        return visited
ans=0

for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            ans=max(ans,len(dfs(i,j,set())))
print(ans)