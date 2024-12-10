N=int(input())
A=list(map(int,input().split()))
D=[0]*N
for i in range(N):
    D[A[i]-1]=i+1
ans=[]
for i in range(1,N+1):
    if i>A[i-1]:
        D[i-1],D[A[i]-1]=D[A[i]-1],D[i-1]
        A[i-1],A[D[i]-1]=A[D[i]-1],A[i-1]
        ans.append([A[i],i])
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])