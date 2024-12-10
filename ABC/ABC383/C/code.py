import sys
sys.setrecursionlimit(10**9)
H,W,D=map(int,input().split())
S=[input() for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
INF=10**18
visited=[[INF for _ in range(W)] for _ in range(H)]
ans=0

from collections import deque

queue=deque()
def bfs():
    while queue:
        x,y=queue.popleft()
        if visited[x][y]==D:
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<H and 0<=ny<W and visited[nx][ny]>visited[x][y]+1 and S[nx][ny]==".":
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))

for i in range(H):
    for j in range(W):
        if S[i][j]=="H":
            visited[i][j]=0
            queue.append((i,j))
bfs()
for i in range(H):
    for j in range(W):
        if visited[i][j]<=D and visited[i][j]!=-1:
            ans+=1
print(ans)

