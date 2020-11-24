import io
import sys

# input here
_INPUT = """\
99 99 99

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

dp = [[[[1] * 300 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in reversed(range(1, 100)):
    for j in reversed(range(1, 100)):
        for k in reversed(range(1, 100)):
            dp[i - 1][j][k] += dp[i][j][k] * (i - 1) / (i + j + k - 1)
            dp[i][j - 1][k] += dp[i][j][k] * (j - 1) / (i + j + k - 1)
            dp[i][j][k - 1] += dp[i][j][k] * (k - 1) / (i + j + k - 1)
