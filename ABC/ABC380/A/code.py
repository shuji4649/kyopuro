N=input()
count=[0,0,0]
for i in range(len(N)):
    n=int(N[i])
    if(0<n<4):
        count[n-1]+=1
ans=True
for i in range(3):
    if count[i]!=(i+1):
        ans=False
        break
print("Yes" if ans else "No")