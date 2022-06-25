import io
import sys

# input here
_INPUT = """\
6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict, deque

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
px = [list(map(int, input().split())) for _ in range(Q)]

G = defaultdict(set)
for idx in range(N - 1):
    A = ab[idx][0] - 1
    B = ab[idx][1] - 1
    G[A].add(B)
    G[B].add(A)

ans = [0] * N
for p, x in px:
    ans[p - 1] += x

def dfs(s):
    dq = deque([s])
    while dq:
        u = dq.pop()
        for v in G[u]:
            if used[v]:
                continue
            used[v] = 1
            dq.append(v)
            ans[v] += ans[u]

used = [0] * N
used[0] = 1
dfs(0)

print(*ans, sep=' ')
