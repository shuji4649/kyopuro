import sys
sys.setrecursionlimit(10**9)
N=int(input())
A=list(map(int,input().split()))
Q=int(input())

INF=10**10
address=dict()
tree=[[0,0,1]]
for i in reversed(range(N)):
    tree.append([A[i],0,0])
    tree[0].append(len(tree)-1)
    address[A[i]]=len(tree)-1
for i in range(Q):
    q=list(map(int,input().split()))

    if q[0]==1:
        x,y=q[1],q[2]
        tree.append([y,address[x],0])
        tree[address[x]].append(len(tree)-1)
        address[y] = len(tree)-1
    if q[0]==2:
        x=q[1]
        tree[address[x]][2]=1
ans=[]
def dfs(now):
    global tree,ans
    if tree[now][2]==0:
        ans.append(tree[now][0])
    for i in reversed(tree[now][3:]):
        dfs(i)
dfs(0)
print(*ans)
    
