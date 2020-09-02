import io
import sys

# input here
_INPUT = """\
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#...
"""
sys.stdin = io.StringIO(_INPUT)



import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
c = [input() for _ in range(H)]

for i, row in enumerate(c):
    for j, grid in enumerate(row):
        if grid == 's':
            s = [i, j]
        elif grid == 'g':
            g = [i, j]

seen = [[0] * W for _ in range(H)]

def dfs(h, w):
    if h < 0 or h > H - 1 or w < 0 or w > W - 1:
        return
    if c[h][w] == '#':
        return
    if seen[h][w] != 0:
        return
    seen[h][w] = 1

    dfs(h + 1, w)
    dfs(h - 1, w)
    dfs(h, w + 1)
    dfs(h, w - 1)


dfs(s[0], s[1])

if seen[g[0]][g[1]] == 1:
    print('Yes')
else:
    print('No')
