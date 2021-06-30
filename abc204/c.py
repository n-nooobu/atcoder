import io
import sys

# input here
_INPUT = """\
4 4
1 2
2 3
3 4
4 1

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    G[A].add(B)

ans = 0
for s in range(N):
    seen = [False] * N
    seen[s] = True
    q = deque([s])
    while q:
        t = q.pop()
        ans += 1
        for w in G[t]:
            if seen[w]:
                continue
            seen[w] = True
            q.append(w)

print(ans)
