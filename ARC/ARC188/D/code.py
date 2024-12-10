T=int(input())
for _ in range(T):
    N=int(input())
    l=len(str(N))
    ans=1
    for i in range(3,l+1,2):

        ans+=1
        ans+=(10**(i//2))*2

    if l%2==1:
        if N<10**(l-1)+10**(l//2)-1:
            ans-=10**(l-1)+10**(l//2)-1-N

    if l%2==0:
        if 10**l-10**(l//2)<=N:
            ans+=N-(10**l-10**(l//2)-1)
        if 10**l-(10**(l//2))*2<=N:
            ans+=1
    print(ans)