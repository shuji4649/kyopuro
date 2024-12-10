S=input()
ans=[]
tmp=0
for i in range(1,len(S)):
    if(S[i]=="|"):
        ans.append(tmp)
        tmp=0
    else:
        tmp+=1
print(*ans)