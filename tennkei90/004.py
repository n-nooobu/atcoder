import io
import sys

# input here
_INPUT = """\
4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

sh = [0] * H
sw = [0] * W
for i in range(H):
    for j in range(W):
        sh[i] += A[i][j]
        sw[j] += A[i][j]

for i in range(H):
    for j in range(W):
        print(sh[i] + sw[j] - A[i][j], end=' ')
    print()
