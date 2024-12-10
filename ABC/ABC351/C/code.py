N=int(input())
A=list(map(int,input().split()))
stock=[]
for i in range(N):
    next=A[i]
    while len(stock)>0 and stock[-1]==next :
        next+=1
        stock.pop()
    stock.append(next)
print(len(stock))