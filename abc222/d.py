import io
import sys

# input here
_INPUT = """\
10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353

dp = [[0] * 3001 for _ in range(N)]
for i in range(a[0], b[0] + 1):
    dp[0][i] = 1

for n in range(1, N):
    s = 0
    for i in range(3001):
        s = (s + dp[n - 1][i]) % mod
        if a[n] <= i <= b[n]:
            dp[n][i] = s % mod

print(sum(dp[-1]) % mod)
