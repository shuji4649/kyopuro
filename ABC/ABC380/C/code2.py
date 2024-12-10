N,K=map(int,input().split())
S=input()
P=[]
if(S[0]=="1"):
    P.append(-1)
P.append(0)
for i in range(1,N):
    if S[i]!=S[i-1]:
        P.append(i)
if(2*K<len(P)):
    ans=S[:P[2*K-2]]+S[P[2*K-1]:P[2*K]]+S[P[2*K-2]:P[2*K-1]]+S[P[2*K]:]
else:
    ans=S[:P[2*K-2]]+S[P[2*K-1]:]+S[P[2*K-2]:P[2*K-1]]
print(ans)

