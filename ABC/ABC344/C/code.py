N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
L=int(input())
C=list(map(int,input().split()))
Q=int(input())
X=list(map(int,input().split()))
av=set()
for i in A:
    for j in B:
        for k in C:
            av.add(i+j+k)
for x in X:
    if x in av:
        print("Yes")
    else:
        print("No")