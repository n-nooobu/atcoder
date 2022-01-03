import io
import sys

# input here
_INPUT = """\
10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, X = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

dp = [[[0] * 2 for j in range(2)] for _ in range(N)]
dp[0][1] = [X // A[0] + 1, (X // A[0] + 1) * A[0] - X]
dp[0][0] = [X // A[0], X % A[0]]
for i in range(N - 1):
    if dp[i][0][0] + dp[i][0][1] // A[i + 1] < dp[i][1][0] + dp[i][1][1] // A[i + 1]:
        dp[i + 1][0][0] = dp[i][0][0] + dp[i][0][1] // A[i + 1]
        dp[i + 1][0][1] = dp[i][0][1] % A[i + 1]
    else:
        dp[i + 1][0][0] = dp[i][1][0] + dp[i][1][1] // A[i + 1]
        dp[i + 1][0][1] = dp[i][1][1] % A[i + 1]

    if dp[i][0][0] + dp[i][0][1] // A[i + 1] + 1 < dp[i][1][0] + dp[i][1][1] // A[i + 1] + 1:
        dp[i + 1][1][0] = dp[i][0][0] + dp[i][0][1] // A[i + 1] + 1
        dp[i + 1][1][1] = (dp[i][0][1] // A[i + 1] + 1) * A[i + 1] - dp[i][0][1]
    else:
        dp[i + 1][1][0] = dp[i][1][0] + dp[i][1][1] // A[i + 1] + 1
        dp[i + 1][1][1] = (dp[i][1][1] // A[i + 1] + 1) * A[i + 1] - dp[i][1][1]

print(min(dp[-1][0][0], dp[-1][1][0]))
