import io
import sys

# input here
_INPUT = """\
2
0 -40
0 40

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ymax = -100
ymin = 100
for i in range(N):
    ymax = max(ymax, xy[i][1])
    ymin = min(ymin, xy[i][1])
