import io
import sys

# input here
_INPUT = """\
3
1000000 999999 999998

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

lcm = 1
for i in range(N):
    lcm = lcm // math.gcd(lcm, A[i]) * A[i]
lcm %= mod

ans = 0
for i in range(N):
    ie = pow(A[i], mod - 2, mod)
    ans += lcm * ie
    ans %= mod

print(ans)
