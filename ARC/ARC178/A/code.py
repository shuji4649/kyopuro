N,M=map(int,input().split())
A=list(sorted(map(int,input().split())))
ans=list(range(1,N+1))
for i in range(M):
    if A[i]==1 or A[i]==N:
        print(-1)
        exit()
    ans[A[i]-1],ans[A[i]]=ans[A[i]],ans[A[i]-1]

print(*ans)
