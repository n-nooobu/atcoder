import io
import sys

# input here
_INPUT = """\
141421 35623
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

mod = 10 ** 9 + 7

a = []
for k in range(K, N + 2):
    start = 10 ** 100 * k + (k - 1) * k // 2
    end = 10 ** 100 * k + (2 * N - k + 1) * k // 2 + 1
    a.append([start, end])

ans = a[0][1] - a[0][0]
for i in range(1, len(a)):
    if a[i][0] > a[i - 1][1]:
        ans += a[i][1] - a[i][0]
    else:
        ans += a[i][1] - a[i - 1][1]
    ans %= mod

print(ans)
