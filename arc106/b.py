import io
import sys

# input here
_INPUT = """\
5 3
0 0 0 0 0
2 2 2 2 2
1 2
2 3
4 5
"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
G = defaultdict(set)
for _ in range(M):
    A, B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

e = [0] + [b[i] - a[i] for i in range(N)]
if sum(e) % 2 == 0:
    color = [0] * (N + 1)
    color[1] = 1
    que = deque([1])
    bipartite = True
    while que:
        p = que.popleft()
        for q in list(G[p]):
            if color[q] == 0:
                color[q] = -color[p]
                que.append(q)
            elif color[q] == color[p]:
                bipartite = False
                break
    black = 0
    white = 0
    for i, col in enumerate(color):
        if i == 0:
            continue
        if col == 1:
            black += e[i]
        elif col == -1:
            white += e[i]

    if black == white:
        print('Yes')
    else:
        print('No')
else:
    print('No')
