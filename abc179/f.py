import io
import sys

# input here
_INPUT = """\
5 5
1 3
2 3
1 4
2 2
1 2
"""
sys.stdin = io.StringIO(_INPUT)



N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

b = (N - 2) ** 2
h = 0
w = 0
for i in range(Q):
    if query[i][0] == 1:
        b -= N - 2 - h
        w += 1
    elif query[i][0] == 2:
        b -= N - 2 - w
        h += 1

print(b)
