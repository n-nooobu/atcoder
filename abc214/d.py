import io
import sys

# input here
_INPUT = """\
5
1 2 1
2 3 2
4 2 5
3 5 14

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
uvw = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for _ in range(N)]
for i in range(N - 1):
    A = uvw[i][0] - 1
    B = uvw[i][1] - 1
    w = uvw[i][2]
    G[A].append([B, w])
    G[B].append([A, w])


