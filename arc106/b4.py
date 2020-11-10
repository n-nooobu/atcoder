import io
import sys

# input here
_INPUT = """\
2 1
1 1
2 1
1 2

"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import defaultdict, deque

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
q = deque([])
while sum(seen) > 0:
    A = 0
    B = 0
    for i in range(N):
        if seen[i]:
            seen[i] = False
            A += a[i]
            B += b[i]
            q.append(i + 1)
            break
    while q:
        t = q.popleft()
        for p in G[t]:
            if not seen[p - 1]:
                continue
            seen[p - 1] = False
            A += a[p - 1]
            B += b[p - 1]
            q.append(p)
    if A != B:
        print('No')
        sys.exit()

print('Yes')
