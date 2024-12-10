S=input()
if S[0]=="<" and S[-1]==">" and S[1:-1]=="="*(len(S)-2):
    print("Yes")
else:   
    print("No")