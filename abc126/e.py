import io
import sys

# input here
_INPUT = """\
100000 1
1 100000 100

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e7))

N, M = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(set)
for i in range(M):
    A = XYZ[i][0] - 1
    B = XYZ[i][1] - 1
    G[A].add(B)
    G[B].add(A)

def dfs(u):
    used[u] = 1
    for v in G[u]:
        if not used[v]:
            dfs(v)

used = [0] * N
ans = 0
for i in range(N):
    if used[i]:
        continue
    dfs(i)
    ans += 1

print(ans)
