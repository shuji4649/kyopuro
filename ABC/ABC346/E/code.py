from collections import defaultdict
H,W,M=map(int,input().split())
hr=set()
wr=set()
query=[]
for _ in range(M):
    T,A,X=map(int,input().split())
    query.append((T,A,X))
d=defaultdict(int)
for t,a,x in reversed(query):
    if t==1:
        if a not in hr:
            d[x]+=W-len(wr)
        hr.add(a)

    else:
        if a not in wr:
            d[x]+=H-len(hr)
        wr.add(a)

    # print(t,a,x,hr,wr,d)
d[0]+=(H-len(hr))*(W-len(wr))
ans_l=list(sorted(d.items(),key=lambda x:x[0]))
ans=[]
for i in ans_l:
    if i[1]>0:
        ans.append((i[0],i[1]))
print(len(ans))
for a in ans:
    print(*a)