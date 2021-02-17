import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(W + 1):
        if j - vw[i - 1][1] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vw[i - 1][1]] + vw[i - 1][0])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
