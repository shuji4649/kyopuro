N=int(input())
S=input()
ans=True
text="1"*((N-1)//2)+"/" + "2"*((N-1)//2)
if(text==S):
    print("Yes")
else:
    print("No")