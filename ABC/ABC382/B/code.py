N,D=map(int,input().split())
S=input()
ans=""
count=0
for i in range(N-1,-1,-1):
    if S[i]=="@" and count<D:
        count+=1
        ans+="."
    else:
        ans+=S[i]
print(ans[::-1])