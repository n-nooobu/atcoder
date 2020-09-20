import io
import sys

# input here
_INPUT = """\
60 3
5 8
1 3
10 15
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]


mod = 998244353
dp = [0] * (N + 1)
dpsum = [0] * (N + 1)
dp[1] = 1
dpsum[1] = 1
for i in range(2, N + 1):
    for j in range(K):
        li = max(i - LR[j][1], 1)
        ri = i - LR[j][0]
        if ri < 0:
            continue
        dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= mod
    dpsum[i] = dpsum[i - 1] + dp[i]

print(dp[N])
