S=input()
T=input().lower()
now=0
for i in range(len(S)):
    if S[i]==T[now]:
        now+=1
        if now==len(T):
            print("Yes")
            exit()
if now==2 and T[2]=="x":
    print("Yes")
else:
    print("No")