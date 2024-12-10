N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=K*(K+1)//2
app=set()
for i in range(N):
    if A[i]<=K:
        app.add(A[i])
print(ans-sum(app))