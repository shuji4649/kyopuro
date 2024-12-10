H,W=map(int,input().split())
A=[input() for _ in range(H)]
N=int(input())
E=[[-1 for _ in range(W)] for _ in range(H)]
for i in range(N):
    R,C,e=map(int,input().split())
    E[R-1][C-1]=e
import sys
sys.setrecursionlimit(10**9)
from collections import deque
d=deque()
start=-1
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            start=(i,j,0,[False for _ in range(H*W)])
            break
    if start!=-1:
        break

d.append(start)
while d:
    x,y,e,visited=d.popleft()
    #print(x,y,e,visited)
    visited[x*W+y]=True
    e=max(e,E[x][y])
    if e==0:
        continue
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if not (0<=nx<H and 0<=ny<W):
            continue
        if visited[nx*W+ny] or A[nx][ny]=="#" :
            continue
        if A[nx][ny]=="T":
            print("Yes")
            exit()
        d.append((nx,ny,e-1,visited[:]))

print("No")

