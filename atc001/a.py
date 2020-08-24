import io
import sys

# input here
_INPUT = """\
4 5
s####
....#
#####
#...g
"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

H, W = map(int, input().split())
c = [input() for _ in range(H)]

dh = [-1, 0, 0, 1]
dw = [0, 1, -1, 0]

for i, row in enumerate(c):
    for j, grid in enumerate(row):
        if grid == 's':
            s = [i, j]
        elif grid == 'g':
            g = [i, j]

seen = [[0] * W for _ in range(H)]
seen[s[0]][s[1]] = 1
q = deque()
q.append(s)

while q:
    th, tw = q.pop()
    for i in range(4):
        nh = th + dh[i]
        nw = tw + dw[i]
        if nh < 0 or nh > H - 1 or nw < 0 or nw > W - 1:
            continue
        if c[nh][nw] == '#':
            continue
        if seen[nh][nw] != 0:
            continue
        seen[nh][nw] = 1
        q.append([nh, nw])

if seen[g[0]][g[1]] == 1:
    print('Yes')
else:
    print('No')
