#UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N,Q=map(int,input().split())

uf=UnionFind(N)
from collections import defaultdict
pOc=dict() # UFの親の色
cOp=defaultdict(int) # 色の数
for i in range(N):
    pOc[i]=i
for i in range(N):
    cOp[i]=1

for i in range(Q):
    query=list(map(int,input().split()))
    if(query[0]==1):
        x,c=query[1]-1,query[2]-1
        cOp[pOc[uf.find(x)]]-=uf.size(x)
        
        cOp[c]+=uf.size(x)
        j=0
        while x+j<N and uf.same(x,x+j):
            j+=1
        if x+j<N and pOc[uf.find(x+j)]==c:
            uf.union(x,x+j)
        
        j=0
        while x-j>=0 and uf.same(x,x-j):
            j+=1
        if x-j>=0 and pOc[uf.find(x-j)]==c:
            uf.union(x,x-j)

        pOc[uf.find(x)]=c
    else:
        c=query[1]-1
        print(cOp[c])
