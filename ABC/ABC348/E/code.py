N=int(input())
Tree=[[] for _ in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a-1].append(b-1)
    Tree[b-1].append(a-1)
P=[0]*N
C=list(map(int,input().split()))
for i in range(N):
    checked=set()
    checked.add(i)
    stack=[(i,0)]
    while stack:
        x,n=stack.pop()
        n+=1
        for y in Tree[x]:
            if y in checked:
                continue
            P[y]+=n*C[i]
            checked.add(y)
            stack.append((y,n))

print(min(P))
    


