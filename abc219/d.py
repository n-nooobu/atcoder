import io
import sys

# input here
_INPUT = """\
3
5 6
2 1
3 4
2 3

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[10 ** 6] * 301 for j in range(301)] for i in range(N + 1)]
dp[1][0][0] = 0
for i in range(1, N + 1):
    for j in range(1, 301):
        for k in range(1, 301):
            if j - AB[i - 1][0] >= 0 and k - AB[i - 1][1] >= 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - AB[i - 1][0]][k - AB[i - 1][1]] + 1)
            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])

ans = 10 ** 6
for i in range(N + 1):
    for j in range(X, 301):
        for k in range(Y, 301):
            ans = min(ans, dp[i][j][k])

if ans == 10 ** 6:
    print(-1)
else:
    print(ans)
