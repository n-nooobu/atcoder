import io
import sys

# input here
_INPUT = """\
4
100 100 100 1000000000
1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[math.inf] * 4 for _ in range(N - 1)]
dp[0][0] = A[0] + A[1] + B[0]
dp[0][2] = A[0]

for i in range(1, N - 1):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + A[i + 1] + B[i]
    dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + A[i + 1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    dp[i][3] = min(dp[i - 1][2], dp[i - 1][3]) + B[i]

ans1 = min(min(dp[-1][0], dp[-1][1]) + B[-1], min(dp[-1][2], dp[-1][3]))

dp = [[math.inf] * 4 for _ in range(N - 1)]
dp[0][1] = A[1]
dp[0][3] = B[0]

for i in range(1, N - 1):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + A[i + 1] + B[i]
    dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + A[i + 1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    dp[i][3] = min(dp[i - 1][2], dp[i - 1][3]) + B[i]

ans2 = min(min(dp[-1][0], dp[-1][1]), min(dp[-1][2], dp[-1][3]) + B[-1])

print(min(ans1, ans2))
