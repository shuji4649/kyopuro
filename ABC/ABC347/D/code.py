a,b,C=map(int,input().split())
c=C.bit_count()
if (a+b-c)%2==0   and a>=(a+b-c)//2 and b>=(a+b-c)//2:
    ansa=0
    ansb=0
    count=0
    countp=0
    for i in range(60):
        if C>>i&1:
            if countp<a-(a+b-c)//2:
                ansa+=1<<i
            else:
                ansb+=1<<i
            countp+=1
        else:
            if count<(a+b-c)//2:
                ansa+=1<<i
                ansb+=1<<i
                count+=1
    if(ansa.bit_count()!=a or ansb.bit_count()!=b or ansa^ansb!=C):
        print(-1)
    else:
        print(ansa,ansb)

else:
    print(-1)
