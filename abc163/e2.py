import io
import sys

# input here
_INPUT = """\
6
8 6 9 1 2 1
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

m = []
for i in range(N):
    m.append([max(A), A.index(max(A))])
    A[A.index(max(A))] = 0

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for l in range(i + 1):
        if l == 0:
            dp[i][0] = dp[i - 1][0] + m[i - 1][0] * (N - 1 - (i - l - 1) - m[i - 1][1])
        elif l == i:
            dp[i][i] = dp[i - 1][i - 1] + m[i - 1][0] * (m[i - 1][1] - (l - 1))
        else:
            tr = dp[i - 1][l] + m[i - 1][0] * (N - 1 - (i - l - 1) - m[i - 1][1])
            tl = dp[i - 1][l - 1] + m[i - 1][0] * (m[i - 1][1] - (l - 1))
            dp[i][l] = max(tr, tl)

print(max(dp[N]))
