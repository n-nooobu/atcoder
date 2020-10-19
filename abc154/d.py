import io
import sys

# input here
_INPUT = """\
10 4
17 13 13 12 15 20 10 13 17 11

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
for i in range(K):
    ans += (p[i] + 1) / 2
old = ans

for i in range(1, N - K + 1):
    new = old - (p[i - 1] + 1) / 2 + (p[i + K - 1] + 1) / 2
    ans = max(ans, new)
    old = new

print(ans)
