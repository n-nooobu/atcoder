import io
import sys

# input here
_INPUT = """\
1111111111111111111

"""
sys.stdin = io.StringIO(_INPUT)



L = input()
mod = 10 ** 9 + 7

dp = [[0] * 2 for _ in range(len(L) + 1)]
dp[0][1] = 1

for i in range(1, len(L) + 1):
    if L[i - 1] == '1':
        dp[i][0] = (dp[i][0] + dp[i - 1][0] * 3) % mod
        dp[i][0] = (dp[i][0] + dp[i - 1][1]) % mod
        dp[i][1] = dp[i - 1][1] * 2 % mod
    else:
        dp[i][0] = (dp[i][0] + dp[i - 1][0] * 3) % mod
        dp[i][1] = dp[i - 1][1]

print((dp[-1][0] + dp[-1][1]) % mod)
