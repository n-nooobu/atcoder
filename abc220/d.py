import io
import sys

# input here
_INPUT = """\
5
0 1 2 3 4


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
mod = 998244353

dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(10):
        dp[i][(j + A[i]) % 10] = (dp[i][(j + A[i]) % 10] + dp[i - 1][j]) % mod
        dp[i][(j * A[i]) % 10] = (dp[i][(j * A[i]) % 10] + dp[i - 1][j]) % mod

for i in range(10):
    print(dp[-1][i])
