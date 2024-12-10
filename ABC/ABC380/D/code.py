S=input()
Q=int(input())
K=list(map(int,input().split()))
L=len(S)
def solve(p):
    ans=0
    k=p-1
    i=k//L
    while i>0:
        ans+=i%2
        i//=2
    if ans%2==1:
        return S[k%L].swapcase()
    else:
        return S[k%L]
ans=[]
for k in K:
    ans.append(solve(k))
print(*ans)       
