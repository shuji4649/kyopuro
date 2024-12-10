N,M=map(int,input().split())
import itertools
ansL=[]
for item in itertools.combinations(range(M-10*N+9+N),N):
    itemL=sorted(list(item))
    ans=[-9]
    errors=[itemL[0]]
    for i in range(1,N):
        errors.append(itemL[i]-itemL[i-1]-1)
    for i in range(N):
        ans.append(ans[-1]+errors[i]+10)
    ansL.append(ans[1:])

print(len(ansL))
for item in ansL:
    print(*item)
