import io
import sys

# input here
_INPUT = """\
3 200
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

mod = 10 ** 9 + 7

X = [0] * (K + 1)
ans = 0
for x in reversed(range(1, K + 1)):
    X[x] = (K // x) ** N - sum([X[x * i] for i in range(2, K // x)])
    ans += X[x] * x
    ans %= mod

print(ans)
