import io
import sys

# input here
_INPUT = """\
2 2 3
1 1 3
2 1 4
1 2 5
"""
sys.stdin = io.StringIO(_INPUT)



R, C, K = map(int, input().split())
rcv = [list(map(int, input().split())) for i in range(K)]

a = [[0] * C for _ in range(R)]
for i in range(K):
    a[rcv[i][0] - 1][rcv[i][1] - 1] = rcv[i][2]

dp = [[[0] * 4 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        for k in reversed(range(4)):
            print(k)

