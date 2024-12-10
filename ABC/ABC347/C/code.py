N,A,B=map(int,input().split())
D=list(map(int,input().split()))
d=set()
for i in range(N):
    d.add(D[i]%(A+B))
d=list(sorted(d))
d.append(d[0]+A+B)
count=0
for i in range(len(d)-1):
    count=max(count,d[i+1]-d[i]-1)
if count>=B:
    print("Yes")
else:
    print("No")