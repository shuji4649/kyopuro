S=input()
N=int(input())
for i in range(N):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    S=S[:l]+S[l:r+1][::-1]+S[r+1:]
print(S)