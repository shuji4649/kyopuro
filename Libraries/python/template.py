############################################################################################

from collections import defaultdict
import math
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
import queue
import time
import random
from decimal import Decimal
from functools import cmp_to_key
import pypyjit 
pypyjit.set_param('max_unroll_recursion=-1')
def I(): return input()
def IS(): return input().split()
def LIS(): return list(input().split())
def II(): return int(input())
def IIS(): return list(map(int, input().split()))
def LIIS(): return list(map(int, input().split()))


sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 998244353
MOD2 = 10**9+7
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res


def yesno(f, yes="Yes", no="No"):
    print(yes if f else no)


def dist(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
dxy8 = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
n16 = "0123456789ABCDEF"
pai=3.141592653589793238
##################################################################

#整数分野
#約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#素数か判定
def isPrime(n):
    if n == 1:
        return False
    for i in range(1, math.ceil(n**0.5)+1):
        if (n % i == 0):
            if i != 1 and n != i:
                return False
    return True

#素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == [] and n > 1:
        arr.append([n, 1])

    return arr

#エラストテネスのふるい(素数列挙)
def sieve_of_erastosthenes(n):
    nums = list(range(n+1))
    for i in range(2, math.floor(n**0.5)+1):
        if nums[i] != 0:
            for j in range(i, n+1):
                if i*j > n:
                    break
                nums[i*j] = 0
    return list(set(nums))[2:]


#UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#転倒数(バブルソートの回数)
def mergecount(A):
    cnt = 0
    n = len(A)
    if n>1:
        A1 = A[:n>>1]
        A2 = A[n>>1:]
        cnt += mergecount(A1)
        cnt += mergecount(A2)
        i1=0
        i2=0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n//2 - i1
    return cnt

