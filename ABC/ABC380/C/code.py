N,K=map(int,input().split())
S=input()
P=[]
tmp=0
tmpN="0"
for i in range(N):
    if S[i]==tmpN:
        tmp+=1
    else:
        P.append(tmp)
        tmp=1
        tmpN=S[i]
P.append(tmp)
ansP=[]
for i in range(len(P)):
    if i==(K*2-3):
        ansP.append(P[i]+P[i+2])
    elif i==(K*2-2):
        if(K*2<len(P)):
            ansP.append(P[i]+P[i+2])
        else:
            ansP.append(P[i])
    elif i==(K*2-1):
        continue
    elif i==(K*2):
        continue
    else:
        ansP.append(P[i])
ans=""
for i in range(len(ansP)):
    if(i%2==0):
        ans+="0"*ansP[i]
    else:
        ans+="1"*ansP[i]
print(ans)