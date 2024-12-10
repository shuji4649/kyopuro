N=int(input())
S=[input() for _ in range(N)]
ans=0
for i in range(N):
    if S[i]=="Takahashi":
        ans+=1

print(ans)