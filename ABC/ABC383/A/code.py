N=int(input())
ans=0
lastT=0
for i in range(N):
    T,V=map(int,input().split())
    if(ans>0):
        ans-=min(ans,T-lastT)
    ans+=V
    lastT=T
print(ans)