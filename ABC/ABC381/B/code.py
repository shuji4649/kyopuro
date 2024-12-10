S=input()
used=set()
if len(S)%2==1:
    print("No")
    exit()
ans=True
for i in range(0,len(S),2):
    if S[i]==S[i+1]:
        if S[i] in used:
            ans=False
            break
        used.add(S[i])
    else:
        ans=False
        break
print("Yes" if ans else "No")