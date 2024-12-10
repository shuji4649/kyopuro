N=int(input())
import math
def sieve_of_erastosthenes(n):
    nums = list(range(n+1))
    for i in range(2, math.floor(n**0.5)+1):
        if nums[i] != 0:
            for j in range(i, n+1):
                if i*j > n:
                    break
                nums[i*j] = 0
    return list(set(nums))[2:]

EL=sieve_of_erastosthenes(int(N**0.125))
ans=len(EL)
sqrtN=int(N**0.5)
NEL=sieve_of_erastosthenes(sqrtN)
for i in range(len(NEL)):
    for j in range(i+1,len(NEL)):
        if NEL[i]*NEL[j]<=sqrtN:
            ans+=1
        else:
            break

print(ans)