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

INF = 10 ** 12
dp = [[INF] * (10 ** 3 * (N + 2)) for _ in range(N + 1)]
dp[0][0] = 0
ans = 0
for i in range(1, N + 1):
    for j in range(len(dp[0])):
        if j - wv[i - 1][1] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - wv[i - 1][1]] + wv[i - 1][0])
        else:
            dp[i][j] = dp[i - 1][j]
        if dp[i][j] <= W:
            ans = max(ans, j)

print(ans)
