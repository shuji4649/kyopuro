A=[]
while True:
    a=int(input())
    A.append(a)
    if a==0:
        break
for i in reversed(A):
    print(i)