import io
import sys

# input here
_INPUT = """\
6 3
2 3
4 5
5 6
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]

dp = [0] * (N + 1)
seen = [0] * (N + 1)
def f(x, dp, seen):
    if seen[x]:
        return dp, seen
    seen[x] = 1
    for i in range(M):
        if xy[i][0] == x:
            dp, seen = f(xy[i][1], dp, seen)
            dp[x] = max(dp[x], dp[xy[i][1]] + 1)
    return dp, seen

ans = 0
for i in range(1, N + 1):
    dp, seen = f(i, dp, seen)
    ans = max(ans, max(dp))
print(max(dp))
