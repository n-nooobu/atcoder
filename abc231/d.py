import io
import sys

# input here
_INPUT = """\
4 3
2 4
4 3
3 2
"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import defaultdict, deque


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(set)
for idx in range(M):
    A = AB[idx][0] - 1
    B = AB[idx][1] - 1
    G[A].add(B)
    G[B].add(A)

for i in range(N):
    if len(G[i]) > 2:
        print('No')
        sys.exit()

used = [0] * N
for s in range(N):
    if used[s]:
        continue
    dq = deque([[s, -1]])
    used[s] = 1
    while dq:
        u, p = dq.pop()
        for v in G[u]:
            if used[v]:
                if v == p:
                    continue
                else:
                    print('No')
                    sys.exit()
            used[v] = 1
            dq.append([v, u])

print('Yes')
