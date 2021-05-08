import io
import sys

# input here
_INPUT = """\
1
12 3 69853


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
DCS = sorted([list(map(int, input().split())) for _ in range(N)])

dp = [[0] * 5001 for _ in range(N)]
for i, (d, c, s) in enumerate(DCS):
    for j in range(5001):
        if i == 0 and j + c <= d:
            dp[i][j + c] = s
            continue
        if j + c > d:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        else:
            dp[i][j + c] = max(dp[i][j], dp[i - 1][j] + s)
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[-1]))
