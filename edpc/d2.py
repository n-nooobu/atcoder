import io
import sys

# input here
_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2

"""
sys.stdin = io.StringIO(_INPUT)



N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(W + 1):
        if j - wv[i - 1][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wv[i - 1][0]] + wv[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
