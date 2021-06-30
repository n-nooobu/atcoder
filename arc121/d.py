import io
import sys

# input here
_INPUT = """\
3
-40 0 20
"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
a = sorted(list(map(int, input().split())))

if N % 2:
    a = sorted(a + [0])

ans = math.inf
while len(a) <= 2 * N:
    ma = -math.inf
    mi = math.inf
    for j in range(len(a) // 2):
        ma = max(ma, a[j] + a[-(j + 1)])
        mi = min(mi, a[j] + a[-(j + 1)])
    ans = min(ans, ma - mi)
    a = sorted(a + [0, 0])

print(ans)
