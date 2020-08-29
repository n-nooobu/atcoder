import io
import sys

# input here
_INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
h = list(map(int, input().split()))

INF = 10 ** 10
dp = [INF] * N
dp[0] = 0
dp[1] = min(dp[1], dp[0] + abs(h[0] - h[1]))

for i in range(2, N):
    if i >= K:
        for j in range(1, K + 1):
            dp[i] = min(dp[i], dp[i - j] + abs(h[i - j] - h[i]))
    else:
        for j in range(1, i + 1):
            dp[i] = min(dp[i], dp[i - j] + abs(h[i - j] - h[i]))

print(dp[N - 1])
