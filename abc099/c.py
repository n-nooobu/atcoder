import io
import sys

# input here
_INPUT = """\
44852

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

INF = 10 ** 5
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    six = 1
    while six <= i:
        dp[i] = min(dp[i], dp[i - six] + 1)
        six *= 6
    nine = 1
    while nine <= i:
        dp[i] = min(dp[i], dp[i - nine] + 1)
        nine *= 9

print(dp[N])
