N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=[]
for i in range(N):
    if A[i]%K==0:
        ans.append(A[i]//K)
print(*ans)