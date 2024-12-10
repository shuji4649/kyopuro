X,Y,Z,P=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
Cmin=C[0]
Cmax=C[-1]
Cmid=(Cmax+Cmin)/2
AthenBC=[0]*X
for i in range(X):
    a=A[i]
    cut=P-a-Cmid
    left=0
    right=Y
    middle=(left+right)//2
    #print(cut)
    while right-left>1:
        b=B[middle]+a+(Cmin if B[middle]<cut else Cmax)
        #print(left,right,middle,b)
        if b>=P:
            right=middle
        else:
            left=middle
        middle=(left+right)//2
    leftB=abs(B[left]+a+(Cmin if B[left]<cut else Cmax)-P)
    if right==Y:
        AthenBC[i]=leftB
        continue
    rightB=abs(B[right]+a+(Cmin if B[right]<cut else Cmax)-P)
    AthenBC[i]=min(leftB,rightB)
print(max(AthenBC))


