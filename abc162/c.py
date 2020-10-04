import io
import sys

# input here
_INPUT = """\
200
"""
sys.stdin = io.StringIO(_INPUT)



import math

K = int(input())

g = [[0] * (K + 1) for _ in range(K + 1)]
for a in range(1, K + 1):
    for b in range(1, K + 1):
        g[a][b] = math.gcd(a, b)

ans = 0
for c in range(1, K + 1):
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            ans += math.gcd(c, g[a][b])

print(ans)
