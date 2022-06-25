import io
import sys

# input here
_INPUT = """\
5
4 5
3 2
5 2
3 1

"""
sys.stdin = io.StringIO(_INPUT)



import sys
sys.setrecursionlimit(int(1e7))

N = int(input())

G = [[] for _ in range(N)]
for idx in range(N - 1):
    u, v = map(int, input().split())
    A = u - 1
    B = v - 1
    G[A].append(B)
    G[B].append(A)

def dfs(u, leaf):
    used[u] = 1
    l, r = -1, -1
    for v in G[u]:
        if not used[v]:
            l1, r1, leaf = dfs(v, leaf)
            if l > 0:
                l = min(l, l1)
                r = max(r, r1)
            else:
                l = l1
                r = r1
    if l == -1:
        l, r = leaf, leaf
        leaf += 1
    ans[u] = [l, r]
    return l, r, leaf

used = [0] * N
ans = [None] * N
dfs(0, 1)

for line in ans:
    print(*line)
