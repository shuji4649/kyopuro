N=int(input())
A=list(map(int,input().split()))
MOD=998244353
FactorialMods=[1]
for i in range(1,MOD+1):
    FactorialMods.append(FactorialMods[-1]*i%MOD)
    
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res
def calc(num):
    if num==1:
        return 1
    return modpow(3,(num-3)//2,MOD)
def countCalc(num):
    return (num-1)//2

ans=1

lastB=0
Counts=[]
Count=0
for i in range(N):
    if A[i]!=A[lastB]:
        ans*=calc(i-lastB)
        Counts.append(countCalc(i-lastB))
        Count+=countCalc(i-lastB)
        print(ans,Counts)
        ans%=MOD
        Count%=MOD
        lastB=i
for i in range(len(Counts)):
    ans*=calc(Counts[i])
    ans%=MOD
    print(ans)
print(ans)