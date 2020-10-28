import io
import sys

# input here
_INPUT = """\
2 2
1 2
3 4
3 4
2 1

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

dp = [[[0] * 2 for _ in range(W)] for _ in range(H)]
dp[0][0][0] =
for i in range(H):
    for j in range(W):
        t = [A[i][j] - B[i][j], B[i][j] - A[i][j]]
        for k in range(2):
            if i > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][0] + t[k])
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][1] + t[k])
            if j > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][0] + t[k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][1] + t[k])

print(abs(min(dp[-1][-1])))
