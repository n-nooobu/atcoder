import io
import sys

# input here
_INPUT = """\
10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, X = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * N
for i in reversed(range(N)):
    cnt[i] += X // A[i]
    X %= A[i]
    if i - 1 >= 0:
        A[i] //= A[i - 1]

dp = [[10 ** 20] * 2 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    if i != N - 1:
        up = A[i + 1]
    else:
        up = 10 ** 20

    dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + cnt[i])

    if cnt[i] + 1 < up:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + cnt[i] + 1)

    if cnt[i] > 0:
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + up - cnt[i])

    dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + up - cnt[i] - 1)

print(dp[-1][0])
