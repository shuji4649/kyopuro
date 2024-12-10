N=int(input())
S=input()

ans=0
for i in range(N):
    if(S[i]=="/"):
        j=1
        while i+j<N and i-j>=0 and S[i+j]=="2" and S[i-j]=="1":
            j+=1
        ans=max(ans,2*j-1)

print(ans)