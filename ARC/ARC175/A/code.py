N,C=map(int,input().split())
A=list(map(int,input().split()))
sumA=[A[0]]
for i in range(N-1):
    sumA.append(sumA[i]+A[i+1])
print(sumA)
ans=0
minA=0
if C>0:
    for i in range(N):
        print(minA,ans)
        minA=min(minA,sumA[i])
        ans=max(ans,sumA[i]-minA)
    print(sumA[N-1]+(C-1)*ans)
else:
    for i in range(N):
        print(minA,ans)
        minA=max(minA,sumA[i])
        ans=min(ans,sumA[i]-minA)
    print(sumA[N-1]+(C-1)*ans)