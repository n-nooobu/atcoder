import io
import sys

# input here
_INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
h = list(map(int, input().split()))

INF = 10 ** 9
dp = [INF] * N
dp[0] = 0
for i in range(N):
    for j in reversed(range(1, K + 1)):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + abs(h[i - j] - h[i]))

print(dp[-1])
