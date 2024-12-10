import bisect
N=int(input())
H=list(map(int,input().split()))
HighPoint=[N-1]
for i in reversed(range(N-1)):
    if H[i]>H[i+1]:
        HighPoint.append(i)

HighPoint.reverse()
print(HighPoint)
sums=[H[i]*(i+1) for i in HighPoint]
print(sums)
sumssums=[0]
for i in range(len(sums)):
    sumssums.append(sumssums[-1]+sums[i])
now=-1
Ii=0
ans=[]
for i in range(N):
    if HighPoint[now+1]<=i:
        now+=1
        ans.append(sumssums[now+1])
        Ii=0
    else:
        Ii+=H[i]
        ans.append(sumssums[now+1]+Ii)
print(ans)
    
