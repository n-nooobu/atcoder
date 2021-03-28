import io
import sys

# input here
_INPUT = """\
7
853983 14095 543053 143209 4324 524361 45154

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
mod = 998244353

ans = A[0] ** 2
S = 0
for i in range(1, N):
    S = (S * 2 + A[i - 1]) % mod
    plus = ((A[i] + S) * A[i]) % mod
    ans = (ans + plus) % mod

print(ans % mod)
