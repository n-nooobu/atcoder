import io
import sys

# input here
_INPUT = """\
1 0 0 0
0 0 1 0
0 0 0 0
1 0 0 0

"""
sys.stdin = io.StringIO(_INPUT)



import itertools
from collections import deque


A = [list(map(int, input().split())) for _ in range(4)]


for j in range(4):
    for k in range(4):
        if A[j][k]:
            sx, sy = k, j

ans = 0
for i in itertools.product([0, 1], repeat=16):
    flg = True
    for j in [5, 6, 9, 10]:
        if i[j] == 0 and i[j - 1] == 1 and i[j + 1] == 1 and i[j - 4] == 1 and i[j + 4] == 1:
            flg = False

    used = [[0] * 4 for _ in range(4)]
    if not i[sy * 4 + sx]:
        continue
    used[sy][sx] = 1
    dq = deque([[sx, sy]])
    while dq:
        ux, uy = dq.pop()
        for vx, vy in [[ux + 1, uy], [ux - 1, uy], [ux, uy + 1], [ux, uy - 1]]:
            if vx < 0 or vx >= 4 or vy < 0 or vy >= 4:
                continue
            if not i[vy * 4 + vx]:
                continue
            if used[vy][vx]:
                continue
            used[vy][vx] = 1
            dq.append([vx, vy])

    for j in range(4):
        for k in range(4):
            if A[j][k]:
                if not used[j][k]:
                    flg = False
            if not used[j][k] == i[j * 4 + k]:
                flg = False

    if flg:
        print(i)
        ans += 1

print(ans)
