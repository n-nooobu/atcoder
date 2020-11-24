import io
import sys

# input here
_INPUT = """\
11 11
S##...#c...
...#d.#.#..
..........#
.#....#...#
#.....bc...
#.##......#
.......c..#
..#........
a..........
d..#...a...
.#........G

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

H, W = map(int, input().split())
a = [input() for _ in range(H)]

moji = [[] for _ in range(30)]
for i in range(H):
    for j in range(W):
        if a[i][j] == 'S':
            s = [i, j]
        if a[i][j] == 'G':
            g = [i, j]
        if 'a' <= a[i][j] <= 'z':
            moji[ord(a[i][j]) - 97].append([i, j])

dh = [-1, 0, 0, 1]
dw = [0, 1, -1, 0]
INF = pow(10, 10)
seen = [[INF] * W for _ in range(H)]
seen[s[0]][s[1]] = 0
q = deque()
q.append([s[0], s[1]])
while q:
    th, tw = q.popleft()
    for i in range(4):
        nh = th + dh[i]
        nw = tw + dw[i]
        if nh < 0 or nh > H - 1 or nw < 0 or nw > W - 1 or a[nh][nw] == '#':
            continue
        if seen[nh][nw] <= seen[th][tw] + 1:
            continue
        seen[nh][nw] = seen[th][tw] + 1
        q.append([nh, nw])
    if 'a' <= a[th][tw] <= 'z':
        for i, (nh, nw) in enumerate(moji[ord(a[th][tw]) - 97]):
            if seen[nh][nw] <= seen[th][tw] + 1:
                continue
            seen[nh][nw] = seen[th][tw] + 1
            q.append([nh, nw])

if seen[g[0]][g[1]] == INF:
    print(-1)
else:
    print(seen[g[0]][g[1]])
