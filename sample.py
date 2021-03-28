import io
import sys

# input here
_INPUT = """\
4 7
1 2
1 3
2 3
2 4
3 2
3 4
4 1
"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict, deque

N, M = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    p = pq[i][0] - 1
    q = pq[i][1] - 1
    G[q].add(p)

path = [[0] * N for _ in range(N)]
for i in range(M):
    path[min(pq[i]) - 1][max(pq[i]) - 1] += 1
for i in range(N):
    for j in range(i + 1, N):
        if path[i][j] != 1:
            print('No')
            exit()

for i in range(N):
    seen = [False] * N
    seen[i] = True
    q = deque([i])
    while q:
        t = q.pop()
        for w in G[t]:
            if seen[w]:
                continue
            seen[w] = True
            q.append(w)
    if sum(seen) < N:
        print('No')
        exit()

print('Yes')
