import io
import sys

# input here
_INPUT = """\
10 3
1
5
4
3
8
6
9
7
2
4
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)
dp[1] = 1
m = 1
for i in range(2, N + 1):
    for j in reversed(range(1, i)):
        if abs(A[i] - A[j]) <= 3:
            if dp[j] == m:
                dp[i] = max(dp[i], dp[j] + 1)
                m = max(m, dp[i])
                break
            else:
                dp[i] = max(dp[i], dp[j] + 1)
                m = max(m, dp[i])

print(max(dp))
