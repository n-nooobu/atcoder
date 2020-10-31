import io
import sys

# input here
_INPUT = """\
8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

distance = []
for i in range(N - 1):
    for j in range(i + 1, N):
        distance.append(((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5)

print(sum(distance) * 2 / N)
