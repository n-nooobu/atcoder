import io
import sys

# input here
_INPUT = """\
7
123456789012345678901234567890
"""
sys.stdin = io.StringIO(_INPUT)



D = int(input())
N = input()
mod = 10 ** 9 + 7

dp = [[[0] * D for _ in range(2)] for _ in range(len(N) + 1)]
dp[0][0][0] = 1

for i in range(len(N)):
    for j in range(D):
        for k in range(10):
            dp[i + 1][1][(j + k) % D] = (dp[i + 1][1][(j + k) % D] + dp[i][1][j]) % mod

        ni = int(N[i])
        for k in range(ni):
            dp[i + 1][1][(j + k) % D] = (dp[i + 1][1][(j + k) % D] + dp[i][0][j]) % mod

        dp[i + 1][0][(j + ni) % D] = (dp[i + 1][0][(j + ni) % D] + dp[i][0][j]) % mod

print(dp[len(N)][0][0] + dp[len(N)][1][0] - 1)
