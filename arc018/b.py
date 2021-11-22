import io
import sys

# input here
_INPUT = """\
3
1 1
2 2
3 3

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1 = xy[j][0] - xy[i][0]
            y1 = xy[j][1] - xy[i][1]
            x2 = xy[k][0] - xy[i][0]
            y2 = xy[k][1] - xy[i][1]
            s = x1 * y2 - x2 * y1
            if s != 0 and s % 2 == 0:
                ans += 1

print(ans)
