import io
import sys

# input here
_INPUT = """\
4 5
1 2
2 5
#.###
####.
#..##
#..##
"""
sys.stdin = io.StringIO(_INPUT)


from collections import deque

H, W = map(int, list(input().split()))
Ch, Cw = map(int, list(input().split()))
Ch -= 1
Cw -= 1
Dh, Dw = map(int, list(input().split()))
Dh -= 1
Dw -= 1
S = [list(input()) for _ in range(H)]

dh = [-1, 0, 0, 1]
dw = [0, 1, -1, 0]

seen = [[None] * W for _ in range(H)]
seen[Ch][Cw] = 0
q = deque()
q.append([Ch, Cw])

while q:
    th, tw = q.pop()
    for i in range(4):
        nh = th + dh[i]
        nw = tw + dw[i]
        if nh < 0 or nh > H - 1 or nw < 0 or nw > W - 1:
            continue
        if S[nh][nw] == '#':
            continue
        if seen[nh][nw] is not None and seen[nh][nw] <= seen[th][tw]:
            continue
        seen[nh][nw] = seen[th][tw]
        q.append([nh, nw])
    for dh2 in range(-2, 3):
        for dw2 in range(-2, 3):
            if dh2 == 0 and dw2 == 0:
                continue
            nh = th + dh2
            nw = tw + dw2
            if nh < 0 or nh > H - 1 or nw < 0 or nw > W - 1:
                continue
            if S[nh][nw] == '#':
                continue
            if seen[nh][nw] is not None and seen[nh][nw] <= seen[th][tw] + 1:
                continue
            seen[nh][nw] = seen[th][tw] + 1
            q.append([nh, nw])

if seen[Dh][Dw] is not None:
    print(seen[Dh][Dw])
else:
    print(-1)
