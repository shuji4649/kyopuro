def twob(n):
    if n==0:
        return 1
    return format(n, 'b')[::-1].find('1')
def twol(n):
    return len(format(n, 'b'))-1
L,R=map(int, input().split())
R-=1
ans=[]
now=L
if now==0:
    ans.append([0,2**twol(R+1)])
    now=2**twol(R+1)
while now<=R:
    next=min(2**twob(now),2**twol(R+1-now))
    ans.append([now,now+next])
    now+=next
print(len(ans))
for i in ans:
    print(*i)

