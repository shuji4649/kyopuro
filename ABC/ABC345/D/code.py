import itertools
N,H,W=map(int, input().split())
Tiles=[list(map(int, input().split())) for _ in range(N)]
def checkEqual(use):
    sa=0
    for i in use:
        sa+=Tiles[i][0]*Tiles[i][1]
    return sa==H*W


def check(H,W,N,a):
    M=[[False for _ in range(W)] for _ in range(H)]
    for i in range(N):
        th,tw,h,w=a[i]
        for j in range(h):
            for k in range(w):
                if M[th+j][tw+k]:
                    return False
                M[th+j][tw+k]=True
    return True
cansolves=[]
for i in range(2**N):
    uses=[]
    for j in range(N):
        if (i>>j)&1:
            uses.append(j)
    if checkEqual(uses):
        cansolves.append(uses)
for cansolve in cansolves:
    loops=[]
    for i in cansolve:
        patterns=[]

        for nnn in range(2):
            h=Tiles[i][0]
            w=Tiles[i][1]
            if nnn==1:
                h,w=w,h
            patterns+=list(itertools.product(range(H-h+1),range(W-w+1),[h],[w]))
        loops.append(patterns)
        
    
    for i in itertools.product(*loops):
        if check(H,W,len(cansolve),i):
            print("Yes")
            exit()
print("No")
        