N,Q=map(int,input().split())
S=input()
Ppoint=[0]*N
slashes=[]
for i in range(N):
    if(S[i]=="/"):
        j=1
        while i+j<N and i-j>=0 and S[i+j]=="2" and S[i-j]=="1":
            j+=1
        Ppoint[i]=j-1
        slashes.append(i)
import bisect
print(Ppoint)
print(slashes)
for i in range(Q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    ans=0
    b_l=bisect.bisect_left(slashes,l)
    b_r=bisect.bisect_right(slashes,r)
    for j in range(b_l,b_r):
        ans=max(ans,min(Ppoint[slashes[j]],min(slashes[j]-l,r-slashes[j])))
        print(b_l,b_r,ans)
    print(2*ans+1)