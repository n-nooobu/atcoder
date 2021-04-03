import io
import sys

# input here
_INPUT = """\
34 6
7
-43 -65
-23 -99
54 -68
65 92
16 83
-18 43
-39 2

"""
sys.stdin = io.StringIO(_INPUT)



x, y = map(int, input().split())
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

def distance(x0, y0, x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = (y1 - y2) * x1 + (x2 - x1) * y1
    return abs(a * x0 + b * y0 + c) / (a ** 2 + b ** 2) ** 0.5

INF = 10 ** 5
ans = INF
for i in range(N - 1):
    d = distance(x, y, xy[i][0], xy[i][1], xy[i+1][0], xy[i+1][1])
    ans = min(ans, d)
d = distance(x, y, xy[0][0], xy[0][1], xy[-1][0], xy[-1][1])
ans = min(ans, d)

print(ans)
