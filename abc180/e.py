import io
import sys

# input here
_INPUT = """\
17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 8
dp = [[INF] * N for _ in range(2 ** N)]
dp[1][0] = 0
for i in range(1, len(dp)):
    if not i & 1:
        continue
    for j in range(N):
        if i & 1 << j:
            continue
        for k in range(N):
            dp[i | 1 << j][j] = min(dp[i | 1 << j][j], dp[i][k] + abs(XYZ[j][0] - XYZ[k][0]) + abs(XYZ[j][1] - XYZ[k][1]) + max(0, XYZ[j][2] - XYZ[k][2]))

ans = INF
for i in range(N):
    ans = min(ans, dp[-1][i] + abs(XYZ[0][0] - XYZ[i][0]) + abs(XYZ[0][1] - XYZ[i][1]) + max(0, XYZ[0][2] - XYZ[i][2]))
print(ans)
