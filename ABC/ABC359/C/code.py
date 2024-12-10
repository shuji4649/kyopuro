S=list(map(int,input().split()))
T=list(map(int,input().split()))
minx=min(S[0],T[0])
miny=min(S[1],T[1])
if minx<0:
    S[0]-=2*minx
    T[0]-=2*minx
if miny<0:
    S[1]-=2*miny
    T[1]-=2*miny

y=abs(S[1]-T[1])
SS=sum(S)%2
TT=sum(T)%2
s_x=(S[0]+S[1]%2)//2+1
t_x=(T[0]+T[1]%2)//2+1
x=abs(s_x-t_x)
if y>x:
    print(y)
    exit()
dist=y
if (S[0]>T[0] and SS==1) or (S[0]<T[0] and SS==0):
    dist+=1
if S[0]>T[0]:
    S[0]-=dist
else:
    S[0]+=dist
S[1]+=y
s_x=(S[0]+S[1]%2)//2+1
t_x=(T[0]+T[1]%2)//2+1
x=abs(s_x-t_x)
print(x+y)