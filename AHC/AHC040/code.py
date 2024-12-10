import random

def query(prdb):
    print(len(prdb))
    for p, r, d, b in prdb:
        print(p, r, d, b)
    W, H = map(int, input().split())
    return W, H

N, T, sigma = map(int, input().split())
wh = [list(map(int, input().split())) for _ in range(N)]

# 0 is smaller
for i in range(N):
    if wh[i][0] < wh[i][1]:
        wh[i] = wh[i][::-1]
        wh[i].append(1)
    else:
        wh[i].append(0)

rng = random.Random(1234)
#wh=sorted(wh,key=lambda x:x[1])
sqrtN=int(N**0.5)

### 1st
prdb = []
for i in range(N):
    prdb.append((
        i,
        wh[i][2],
        'U',
        -1 if i%sqrtN==0 else i-1
        
    ))
query(prdb)

### 2nd
for _ in range(T-1):
    prdb = []
    for i in range(N):
        prdb.append((
            i,
            wh[i][2],
            'L',
            -1 if i%sqrtN==0 else i-1
        ))
    query(prdb)
