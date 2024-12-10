import math
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    gcdNK=math.gcd(N,K)
    if gcdNK>2:
        print("No")
        continue
    if N%2==0:
        if (N//2)%2==1:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
