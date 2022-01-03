import io
import sys

# input here
_INPUT = """\
1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)



H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mod = 998244353

dp = [[0] * 4 for _ in range(K + 1)]
dp[1] = [0, 1, 1, 0]
dp[2] = [H + W - 2, H - 2, W - 2, 2]
for i in range(3, K + 1):
    dp[i][0] = (dp[i - 1][1] * (H - 1) + dp[i - 1][2] * (W - 1)) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * (H - 2) + dp[i - 1][3] * (W - 1)) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][2] * (W - 2) + dp[i - 1][3] * (H - 1)) % mod
    dp[i][3] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] * (H + W - 4)) % mod

if x1 == x2 and y1 == y2:
    print(dp[-1][0])
elif y1 == y2:
    print(dp[-1][1])
elif x1 == x2:
    print(dp[-1][2])
else:
    print(dp[-1][3])
