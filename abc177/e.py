import io
import sys

# input here
_INPUT = """\
3
6 10 16

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
A = list(map(int, input().split()))

a = A[0]
for i in range(1, N):
    a = math.gcd(a, A[i])
if a != 1:
    print('not coprime')
    exit()

def get_spf(n):
    spf = [i for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if spf[p] == p:
            for q in range(2 * p, n + 1, p):
                if spf[q] == q:
                    spf[q] = p
        p += 1
    return spf

spf = get_spf(10 ** 6)
factors = set()
for i in range(N):
    tmp = set()
    a = A[i]
    while a > 1:
        tmp.add(spf[a])
        a //= spf[a]
    for j in tmp:
        if j in factors:
            print('setwise coprime')
            exit()
        factors.add(j)

print('pairwise coprime')
