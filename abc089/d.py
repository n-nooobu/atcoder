import io
import sys

# input here
_INPUT = """\
5 5 4
13 25 7 15 17
16 22 20 2 9
14 11 12 1 19
10 6 23 8 18
3 21 5 24 4
3
13 13
2 10
13 13


"""
sys.stdin = io.StringIO(_INPUT)



H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

p = [[0] * 2 for _ in range(H * W + 1)]
for i in range(H):
    for j in range(W):
        p[A[i][j]] = [i, j]

q = [0] * (H * W + 1)
for i in range(H * W, -1, -1):
    if i > H * W - D:
        continue
    q[i] = q[i+D] + abs(p[i][0]-p[i+D][0]) + abs(p[i][1]-p[i+D][1])

for l, r in LR:
    print(q[l] - q[r])
