N,L,T=map(int,input().split())  
A=list(map(int,input().split()))
S=list(map(int,input().split()))
Q=int(input())
Member=[0]*L
Count=[0]*L

for i in range(N):
    Member[A[i]-1].append(S[i])

for i in range(Q):
    x,y=map(int,input().split())
    x-=1
    Member[x]
