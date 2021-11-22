import io
import sys

# input here
_INPUT = """\
4
1 2
1 0
4 0
0 0
"""
sys.stdin = io.StringIO(_INPUT)



from fractions import Fraction

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

edge = set()
for i in range(N):
    for j in range(i + 1, N):
        if xy[i][1] - xy[j][1] == 0:
            edge.add(10 ** 10)
        else:
            edge.add(Fraction(xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]))

print(len(edge) * 2)
