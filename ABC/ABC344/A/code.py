S=input()
ans=""
flag=False
for i in range(len(S)):
    if S[i]=="|":
        flag=not flag
        continue
    if flag==False:
        ans+=S[i]
print(ans)