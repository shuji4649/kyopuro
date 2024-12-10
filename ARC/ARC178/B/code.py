T=int(input())
mod=998244353
for _ in range(T):
    A1,A2,A3=map(int,input().split())
    if A1==A2==A3:
        p=9*(10**(A1-1))%mod
        print((p*(p-1))%mod//2)
    elif max(A1,A2)+1<=A3:
        print(0)
    elif max(A1,A2)==A3:
        a1=max(A1,A2)
        a2=min(A1,A2)
        p=(10**a2)*
        print((p*(p-1))%mod)
    
    
