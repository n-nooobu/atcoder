import io
import sys

# input here
_INPUT = """\
100 5
1
23
45
67
89


"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
mod = 10 ** 9 + 7

dp = [0] * (N + 1)
ng = [False] * (N + 1)
for i in range(M):
    a = int(input())
    ng[a] = True

dp[0] = 1
if not ng[1]:
    dp[1] = 1
for i in range(2, N+1):
    if not ng[i]:
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[-1])
