S=input()
from collections import defaultdict
d=defaultdict(int)
for i in range(len(S)):
    d[S[i]]+=1
p=defaultdict(int)
for k,s in d.items():
    p[s]+=1
for i in p.values():
    if i==0 or i==2:
        continue
    else:
        print("No")
        exit()
print("Yes")
