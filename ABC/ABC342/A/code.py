S=input()
ans=0
now=S[0] if S[0]==S[1] else S[2]
for i in range(len(S)):
    if S[i]!=now:
        print(i+1)
        break