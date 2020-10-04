import io
import sys

# input here
_INPUT = """\
4 5
1 2
1 3
3 2
2 4
3 4
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]

def dfs(p):
    if v[p]:
        return dp[p]
    v[p] = True
    for i in xy:
        if not v[i]:
            dfs(i)
        dp[p] = max(dp[p], dp[i] + 1)

v = [False] * (N + 1)
dp = [0] * (N + 1)

