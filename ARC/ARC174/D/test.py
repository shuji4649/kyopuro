ans=0
for i in range(1,1000000000):
    x2=i
    x=int(i**0.5)
    if str(x2).startswith(str(x)):
        ans+=1
        print(x,x2,ans)