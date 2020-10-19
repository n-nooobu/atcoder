import io
import sys

# input here
_INPUT = """\
2
0 0 0
1 2 3

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 8
dp = [INF] * (2 ** N + 1)
dp[1] = 0

last = [0] * (2 ** N + 1)
for i in range(2 ** N + 1):
    if dp[i] == INF:
        continue
    for j in range(N):
        if i & 1 << j:
            continue
        if dp[i | 1 << j] > dp[i] + abs(XYZ[j][0] - XYZ[last[i]][0]) + abs(XYZ[j][1] - XYZ[last[i]][1]):
            dp[i | 1 << j] = dp[i] + abs(XYZ[last[i]][0]) + abs(XYZ[last[i]][1])
            last[i | 1 << j] = j

ans = dp[-2]
for i in range(1, N):
    if XYZ[i][2] > XYZ[0][2]:
        ans += XYZ[i][2]

print(ans)
