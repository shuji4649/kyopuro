N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Al=[]
Ali=[]
for i in range(N):
    if i==0:
        Al.append(A[i])
        Ali.append(i)
    else:
        if A[i]<Al[-1]:
            Al.append(A[i])
            Ali.append(i)
Al=Al[::-1]
Ali=Ali[::-1]
import bisect
for b in B:
    p=bisect.bisect_right(Al,b)
    if p==0:
        print(-1)
    else:
        print(Ali[p-1]+1)