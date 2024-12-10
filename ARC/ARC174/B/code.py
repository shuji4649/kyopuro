def of1(n):
    if n==0:
        return 1
    return (2**((n-1)%4+1))%10
def solve(N,M,K):
    if N<K:
        return of1(N)
    N-=K
    M-=K

    if M==1:
        return 0
    if N<M:
        #print(of1(N),of1(K))

        return of1(N)*of1(K)%10
    else:
        #print(of1(M),of1(N%M),of1(K))
        return (of1(N%M))*of1(K)%10
    
    
T=int(input())
for _ in range(T):
    N,M,K=map(int,input().split())
    print(solve(N,M,K))