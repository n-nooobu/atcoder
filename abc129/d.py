import io
import sys

# input here
_INPUT = """\
8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]

L = [[0] * W for _ in range(H)]
for i in range(H):
    streak = 0
    for j in range(W):
        if S[i][j] == '.':
            streak += 1
        else:
            streak = 0
        L[i][j] = streak

R = [[0] * W for _ in range(H)]
for i in range(H):
    streak = 0
    for j in reversed(range(W)):
        if S[i][j] == '.':
            streak += 1
        else:
            streak = 0
        R[i][j] = streak

U = [[0] * W for _ in range(H)]
for j in range(W):
    streak = 0
    for i in range(H):
        if S[i][j] == '.':
            streak += 1
        else:
            streak = 0
        U[i][j] = streak

D = [[0] * W for _ in range(H)]
for j in range(W):
    streak = 0
    for i in reversed(range(H)):
        if S[i][j] == '.':
            streak += 1
        else:
            streak = 0
        D[i][j] = streak

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)

print(ans)
