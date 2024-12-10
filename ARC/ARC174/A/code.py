N,M=map(int,input().split())
B=[[0 for _ in range(N)]for _ in range(N)]
hols=[]
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    B[a][b]=1
    hols.append((a,b))
deletes=set()
ups=[]

def intheline(y,x,N,M):
    if y<=x<y+M:
        return True
    if x<y+M-N:
        return True
    return False
for x,y in hols:
    print(x,y)
    if not intheline(x,y,N,M):
        xj,yj=-1,-1
        for j in range(N):
            if intheline(j,y,N,M) and ((j,y) not in hols) and ((j,y) not in deletes) :
                deletes.add((j,y))
                xj=j
                break
        for j in range(N):
            if intheline(x,j,N,M) and ((x,j) not in hols) and ((x,j) not in deletes):
                deletes.add((x,j))
                yj=j
                break
        ups.append((x,y))
        ups.append((xj,yj))
    print(deletes,ups)


print(N*M)
for i in range(N):
    for j in range(N):
        if intheline(i,j,N,M):
            if (i,j) not in deletes:
                print(i+1,j+1)
for i in ups:
    print(i[0]+1,i[1]+1)
        
