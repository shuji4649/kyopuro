N,D=map(int,input().split())
S=input()
ans=D
for i in range(N):
    if S[i]==".": ans+=1
print(ans)