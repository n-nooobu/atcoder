import io
import sys

# input here
_INPUT = """\
4 2
2 3
0 0
0 1
1 2
2 0

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    if i + 1 in A:
        continue
    dist_min = 10 ** 7
    for j in A:
        j -= 1
        dist = ((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2) ** 0.5
        dist_min = min(dist_min, dist)
    ans = max(ans, dist_min)

print(ans)
