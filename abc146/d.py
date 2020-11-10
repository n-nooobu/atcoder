import io
import sys

# input here
_INPUT = """\
6
1 2
1 3
1 4
1 5
1 6

"""
sys.stdin = io.StringIO(_INPUT)



from copy import deepcopy
from collections import defaultdict, deque, OrderedDict

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
G = defaultdict(set)
for i in range(N - 1):
    A = ab[i][0]
    B = ab[i][1]
    G[A].add(B)
    G[B].add(A)

K = 0
for i in range(len(G)):
    K = max(K, len(G[i]))
color = OrderedDict()
for i in range(1, K + 1):
    color[str(i)] = i

edge_color = [[0] * (N + 1) for _ in range(N + 1)]
seen = [False] * (N + 1)
q = deque([])
seen[1] = True
q.append([1, 0])
while q:
    t = q.popleft()
    c = deepcopy(color)
    if t[1] != 0:
        del c[str(t[1])]
    for p in G[t[0]]:
        if seen[p]:
            continue
        seen[p] = True
        edge_color[t[0]][p] = c[list(c.keys())[0]]
        edge_color[p][t[0]] = c[list(c.keys())[0]]
        q.append([p, c[list(c.keys())[0]]])
        del c[list(c.keys())[0]]

print(K)
for i in range(N - 1):
    print(edge_color[ab[i][0]][ab[i][1]])
