wW,bB=map(int,input().split())
W=wW-7*min(wW//7,bB//5)
B=bB-5*min(wW//7,bB//5)

piano="wbwbwwbwbwbwwbwbwwbwbwbw"
for i in range(24-(W+B)+1):
    w=0
    b=0
    for s in piano[i:i+(W+B)]:
        if s=="w":
            w+=1
        else:
            b+=1
    if w==W and b==B:
        print("Yes")
        exit()  
print("No")
