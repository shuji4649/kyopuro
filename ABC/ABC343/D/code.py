N=int(input())
A=list(map(int,input().split()))
A.sort()


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == [] and n > 1:
        arr.append([n, 1])

    return arr
from collections import defaultdict
B=defaultdict(int)
zero=0
for i in A:
    if i==0:
        zero+=1
        continue
    d=factorization(i)
    tmp=[]
    for x,y in d:
        if y%2==1:
            tmp.append(x)
    B[tuple(tmp)]+=1

ans=0
for i in B.values():
    if i>1:
        ans+=i*(i-1)//2
print(ans+zero*(N-zero)+zero*(zero-1)//2)
    
