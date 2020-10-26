import io
import sys

# input here
_INPUT = """\
2 1
0 0
1 0
1 2
"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cd = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    A = cd[i][0]
    B = cd[i][1]
    G[A].add(B)
    G[B].add(A)

seen = [True] * N
e = [0] + [b[i] - a[i] for i in range(N)]
color = [0] * (N + 1)
que = deque([])
while sum(seen) != 0:
    color = [0] * (N + 1)
    for i in range(N):
        if seen[i]:
            que.append(i + 1)
            seen[i] = False
            color[i + 1] = 1
    while que:
        p = que.popleft()
        for q in list(G[p]):
            if color[q] == 0:
                color[q] = -color[p]
                que.append(q)
                seen[q - 1] = False
    s = 0
    for i in range(N + 1):
        if color[i] == 1 or color[i] == -1:
            s += e[i]
    if s % 2 == 1:
        print('No')
        sys.exit()
    black = 0
    white = 0
    for i, col in enumerate(color):
        if i == 0:
            continue
        if col == 1:
            black += e[i]
        elif col == -1:
            white += e[i]

    if black != white:
        print('No')
        sys.exit()

print('Yes')
