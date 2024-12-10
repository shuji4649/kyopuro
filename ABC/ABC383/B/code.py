H,W,D=map(int,input().split())
S=[input() for _ in range(H)]
ans=0
for x1 in range(H):
    for y1 in range(W):
        for x2 in range(H):
            for y2 in range(W):
                if x1==x2 and y1==y2:
                    continue
                if S[x1][y1]=="#" or S[x2][y2]=="#":
                    continue
                count=set()
                for i in range(D+1):
                    for j in range(D+1-i):
                        if 0<=x1+i<H and 0<=y1+j<W and S[x1+i][y1+j]==".":
                            count.add((x1+i,y1+j))
                        if 0<=x1+i<H and 0<=y1-j<W and S[x1+i][y1-j]==".":
                            count.add((x1+i,y1-j))
                        if 0<=x1-i<H and 0<=y1+j<W and S[x1-i][y1+j]==".":
                            count.add((x1-i,y1+j))
                        if 0<=x1-i<H and 0<=y1-j<W and S[x1-i][y1-j]==".":
                            count.add((x1-i,y1-j))
                        if 0<=x2+i<H and 0<=y2+j<W and S[x2+i][y2+j]==".":
                            count.add((x2+i,y2+j))
                        if 0<=x2+i<H and 0<=y2-j<W and S[x2+i][y2-j]==".":
                            count.add((x2+i,y2-j))
                        if 0<=x2-i<H and 0<=y2+j<W and S[x2-i][y2+j]==".":
                            count.add((x2-i,y2+j))
                        if 0<=x2-i<H and 0<=y2-j<W and S[x2-i][y2-j]==".":
                            count.add((x2-i,y2-j))
                ans=max(ans,len(count))
print(ans)
                            
