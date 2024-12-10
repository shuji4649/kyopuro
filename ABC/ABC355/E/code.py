N=int(input())
Gu=[]
Ki=[]
for i in range(N):
    x,y=map(int,input().split())
    if (x+y)%2==0:

        Gu.append((x,y))
    else:

        Ki.append((x,y))
ans=0
for i in range(len(Gu)):
    for j in range(i+1,len(Gu)):
        ans+=max(abs(Gu[i][0]-Gu[j][0]),abs(Gu[i][1]-Gu[j][1]))

for i in range(len(Ki)):
    for j in range(i+1,len(Ki)):
        ans+=max(abs(Ki[i][0]-Ki[j][0]),abs(Ki[i][1]-Ki[j][1]))
print(ans)