N,Q=map(int,input().split())
T=list(map(int,input().split()))
te=[True]*N
ans=0
for i in range(Q):
    te[T[i]-1]=not te[T[i]-1]
for i in range(N):
    if te[i]:
        ans+=1
print(ans)
