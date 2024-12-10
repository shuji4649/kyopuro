N=int(input())
C=[list(map(int,input().split())) for _ in range(N)]
from collections import defaultdict
from itertools import combinations

import copy
f_d=defaultdict(set)
b_d=defaultdict(set)
for i in range(N):
    f_d[C[i][0]].add(i)
    b_d[C[i][1]].add(i)
memo=defaultdict(set)
def dfs(fd,bd,times,used):
    global memo
    returnans=set()
    if used in memo.keys():
        return memo[used]
    for k,il in fd.items():
        if len(il)>=2:
            for i,j in combinations(il,2):
                fd_n=copy.deepcopy(fd)
                fd_n[k].remove(i)
                fd_n[k].remove(j)
                bd_n=copy.deepcopy(bd)
                bd_n[C[i][1]].remove(i)
                bd_n[C[j][1]].remove(j)
                returnans.add(dfs(fd_n,bd_n,times+1,used+2**i+2**j))
    for k,il in bd.items():
        if len(il)>=2:
            for i,j in combinations(il,2):
                bd_n=copy.deepcopy(bd)
                bd_n[k].remove(i)
                bd_n[k].remove(j)
                fd_n=copy.deepcopy(fd)
                fd_n[C[i][0]].remove(i)
                fd_n[C[j][0]].remove(j)
                returnans.add(dfs(fd_n,bd_n,times+1,used+2**i+2**j))
    returntext=""
    if returnans==set():
        returntext= "Takahashi" if times%2==1 else "Aoki"
    else:
        if times%2==0:
            if "Takahashi" in returnans:
                returntext= "Takahashi"
            elif len(returnans)==1 and "Aoki" in returnans:
                returntext= "Aoki"
            else:
                returntext= "None"
        else:
            if "Aoki" in returnans:
                returntext= "Aoki"
            elif len(returnans)==1 and "Takahashi" in returnans:
                returntext= "Takahashi"
            else:
                returntext= "None"
    #print(fd,bd,times,returntext,returnans)
    memo[used]=returntext
    return returntext
print(dfs(f_d,b_d,0,0))
