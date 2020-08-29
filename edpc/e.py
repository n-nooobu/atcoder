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
wv = [list(map(int, input().split())) for i in range(N)]

INF = 10 ** 10
dp = [[INF] * (N * 1000 + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(N * 1000 + 1):
        if j <= wv[i - 1][1]:
            dp[i][j] = min(dp[i][j], wv[i - 1][0])
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - wv[i - 1][1]] + wv[i - 1][0])
        dp[i][j] = min(dp[i][j], dp[i - 1][j])

ans = 0
for i in range(N * 1000 + 1):
    if dp[N][i] <= W:
        ans = max(ans, i)
print(ans)
