import io
import sys

# input here
_INPUT = """\
5 5
1 1 1 1 1
2 2 2 2 2

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[10 ** 10] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N + 1):
    for j in range(M + 1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        if i > 0 and j > 0:
            if A[i - 1] == B[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

print(dp[-1][-1])
