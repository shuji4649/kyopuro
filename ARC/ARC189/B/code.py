N=int(input())
X=list(map(int,input().split()))
D1=[]
for i in range(0,N-1,2):
    D1.append(X[i+1]-X[i])
D2=[]
for i in range(1,N-1,2):
    D2.append(X[i+1]-X[i])
D1.sort()
D2.sort()

ans=X[0]
now=X[0]
for i in range(N-1):
    if i%2==0:
        now+=D1[i//2]
    else:
        now+=D2[i//2]
    ans+=now
print(ans)
