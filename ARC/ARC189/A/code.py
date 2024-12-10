N=int(input())
A=list(map(int,input().split()))
MOD=998244353
FactorialMods=[0]*N
FactorialMods[0]=1
FactorialMods[1]=1
finv=[0]*N
finv[0]=1
finv[1]=1
inv=[0]*N
inv[1]=1
for i in range(2,N):
    FactorialMods[i]=(FactorialMods[i-1]*i%MOD)
    inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i]=(finv[i-1]*inv[i]%MOD)
FACFAC=[0,1]
for i in range(3,N+2,2):
    FACFAC.append(0)
    FACFAC.append(FACFAC[-2]*(i-2)%MOD)
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res
def countCalc(num):
    return (num-1)//2

ans=1

lastB=0
Counts=[]
Count=0
for i in range(N):
    if A[i]!=A[lastB]:
        if i%2==A[i]%2:
            print(0)
            exit()
        ans*=FACFAC[i-lastB]
        Counts.append(countCalc(i-lastB))
        Count+=countCalc(i-lastB)
        ans%=MOD
        Count%=MOD
        lastB=i
ans*=FACFAC[N-lastB]
Counts.append(countCalc(N-lastB))
Count+=countCalc(N-lastB)
ans%=MOD
Count%=MOD

ans*=FactorialMods[Count]
ans%=MOD
for i in range(len(Counts)):
    ans*=finv[Counts[i]]
    ans%=MOD
print(ans)
