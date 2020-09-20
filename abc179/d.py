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

l = []
for i in range(K):
    for j in range(LR[i][1] - LR[i][0] + 1):
        l.append(LR[i][0] + j)

dp = [0] * N
dp[0] = 1
for i in range(N):
    for j in range(len(l)):
        if i + l[j] < N:
            dp[i + l[j]] += dp[i]

print(dp[N - 1] % 998244353)
