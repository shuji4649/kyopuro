N=int(input())
S=input()
al=list(set([i]) for i in range(26))  #last i

alpha="abcdefghijklmnopqrstuvwxyz"

Q=int(input())

for i in range(Q):
    c,d=input().split()
    al[alpha.index(d)] |= al[alpha.index(c)]
    if c!=d:
        al[alpha.index(c)]=set()

nal=[0 for _ in range(26)]
for i in range(26):
    for j in al[i]:
        nal[j]=i

ans=""
for i in range(N):
    now=nal[alpha.index(S[i])]
    ans+=alpha[now]
print(ans)