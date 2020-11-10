import io
import sys

# input here
_INPUT = """\
10 100
15 23
20 18
13 17
24 12
18 29
19 27
23 21
18 20
27 15
22 25

"""
sys.stdin = io.StringIO(_INPUT)



N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])

dp = [[0] * T for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(AB[i - 1][0], T):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - AB[i - 1][0]] + AB[i - 1][1])

ans = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        ans = max(ans, dp[i][-1] + AB[i][1])

print(ans)
