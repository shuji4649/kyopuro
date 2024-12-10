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

N,K=map(int,input().split())
S=input()
MOD=998244353
S_l=list(S)
uf=UnionFind(N)
for i in range(N-K+1):
    tmp1=[]
    tmp2=[]
    tmp3=[]
    for j in range(K//2):
        if S[i+j]!=S[i+K-1-j]:
            break
        if S[i+j]=="?" and S[i+K-1-j]!="?":
            tmp1.append(j)
        elif S[i+j]!="?" and S[i+K-1-j]=="?":
            tmp2.append(j)
        elif S[i+j]=="?" and S[i+K-1-j]=="?":
            tmp3.append(j)
    else:
        for j in tmp1:
            S_l[i+j]=S[i+K-1-j]
        for j in tmp2:
            S_l[i+K-1-j]=S[i+j]
        for j in tmp3:
            if S[i+j]!="?":
                S_l[i+K-1-j]=S[i+j]
            elif S[i+K-1-j]!="?":
                S_l[i+j]=S[i+K-1-j]
            else:
                uf.union(i+j,i+K-1-j)
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res

count=0
for i in range(N):
    if S_l[i]=="?":
        count+=1
ans=modpow(2,count,MOD)
print(ans,count)

for i in uf.roots():
    if S_l[i]!="?":
        continue
    tmp=modpow(2,uf.size(i),MOD)
    print(i,uf.size(i),tmp)
    ans=ans*modpow(tmp,MOD-2,MOD)%MOD
print(ans)
