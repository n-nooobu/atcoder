import io
import sys

# input here
_INPUT = """\
8 3 2


"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict, deque

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

G = defaultdict(set)
for i in range(M):
    A = ab[i][0]
    B = ab[i][1]
    G[A].add(B)

seen = [False] * (N + 1)
q = deque()
loop = []
for s in range(1, N + 1):
    if seen[s]:
        continue
    seen[s] = True
    q.append([s, []])
    while q:
        t, path = q.pop()
        for w in G[t]:
            if seen[w]:
                if path[-1] == w:
                    loop.append(path )
            seen[w] = True
            q.append(w)
