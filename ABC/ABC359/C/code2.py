S=list(map(int,input().split()))
T=list(map(int,input().split()))
if S[0]>T[0]:
    S,T=T,S
y=abs(S[1]-T[1])
SS=sum(S)%2
TT=sum(T)%2
dist=y
if (S[0]>T[0] and SS==1) or (S[0]<T[0] and SS==0):
    dist+=1

S[0]+=dist
S[1]=T[1]
if S[0]>=T[0]:
    print(y)
else:
    s_x=(S[0]+S[1]%2)//2+1
    t_x=(T[0]+T[1]%2)//2+1
    x=abs(s_x-t_x)
    print(x+y)
