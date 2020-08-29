import io
import sys

# input here
_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(abs(h[i - 2] - h[i]) + dp[i - 2], abs(h[i - 1] - h[i]) + dp[i - 1])

print(dp[-1])
