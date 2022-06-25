import io
import sys

# input here
_INPUT = """\
3
8 8
3 4
2 3
2 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[10 ** 6] * (Y + 1) for j in range(X + 1)] for i in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(X + 1):
        for k in range(Y + 1):
            dp[i + 1][min(X, j + AB[i][0])][min(Y, k + AB[i][1])] \
                = min(dp[i + 1][min(X, j + AB[i][0])][min(Y, k + AB[i][1])], dp[i][j][k] + 1)
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

if dp[N][X][Y] == 10 ** 6:
    print(-1)
else:
    print(dp[N][X][Y])
