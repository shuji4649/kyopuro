def solve():
    A=list(map(int,input().split()))
    P=list(map(int,input().split()))
    N=sum(A)
    psum=sum([(i+1)*A[i] for i in range(5)])
    if psum>N*3:
        return 0
    plus=N*3-psum
    return min(P[3]*2,P[4])*(plus//2)+min(P[3],P[4])*(plus%2)
T=int(input())
for i in range(T):
    print(solve())