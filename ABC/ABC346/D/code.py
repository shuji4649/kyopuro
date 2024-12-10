N=int(input())
S=input()
C=list(map(int,input().split()))
start1_f=[0]
start1_b=[0]
start0_f=[0]
start0_b=[0]
for i in range(N):
    if i%2==int(S[i]):
        start1_f.append(start1_f[-1]+C[i])
        start0_f.append(start0_f[-1]+0)
    else:
        start1_f.append(start1_f[-1]+0)
        start0_f.append(start0_f[-1]+C[i])
    if (N-1-i)%2!=int(S[N-1-i]):
        start1_b.append(start1_b[-1]+C[N-1-i])
        start0_b.append(start0_b[-1]+0)
    else:
        start1_b.append(start1_b[-1]+0)
        start0_b.append(start0_b[-1]+C[N-1-i])
ans=10**18
for i in range(N-1):
    ans=min(ans,start0_f[i+1]+start0_b[N-1-i],start1_f[i+1]+start1_b[N-1-i])
print(ans)