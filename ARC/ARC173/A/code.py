T=int(input())
INF=10**14
def neq(n):
    ans=0
    bef=0
    flag=1
    for i in range(len(str(n))):
        if bef<int(str(n)[i]):
            ans+=(int(str(n)[i])-1)*(9**(len(str(n))-i-1))
        else:
            ans+=int(str(n)[i])*(9**(len(str(n))-i-1))
        if bef==int(str(n)[i]):
            flag=0
            break
        bef=int(str(n)[i])
    for i in range(len(str(n))-1):
        ans+=9**(i+1)
    return ans+flag

for _ in range(T):
    K=int(input())
    left=0
    right=INF
    middle=(left+right)//2
    while left+1<right:
        #print(left,right,middle,neq(middle))
        middle=(left+right)//2
        if neq(middle)<K:
            left=middle
        else:
            right=middle
    print(right)