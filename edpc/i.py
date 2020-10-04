import io
import sys

# input here
_INPUT = """\
5
0.42 0.01 0.42 0.99 0.42
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
p = [0] + list(map(float, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][0] = 1 - p[1]
dp[1][1] = p[1]
for i in range(2, N + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * (1 - p[i])
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] * p[i]
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p[i]) + dp[i - 1][j - 1] * p[i]

print(sum(dp[N][N // 2 + 1:]))
