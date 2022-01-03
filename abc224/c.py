import io
import sys

# input here
_INPUT = """\
20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1 = XY[j][0] - XY[i][0]
            y1 = XY[j][1] - XY[i][1]
            x2 = XY[k][0] - XY[i][0]
            y2 = XY[k][1] - XY[i][1]
            if x1 * y2 != x2 * y1:
                ans += 1

print(ans)
