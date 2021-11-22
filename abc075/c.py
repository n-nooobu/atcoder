import io
import sys

# input here
_INPUT = """\
6 5
1 2
2 3
3 4
4 5
5 6

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e7))

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]


def dfs(u):
    used[u] = 1
    for v in G[u]:
        if not used[v]:
            dfs(v)


ans = 0
for i in range(M):
    G = defaultdict(set)
    for j in range(M):
        if i == j:
            continue
        A = ab[j][0] - 1
        B = ab[j][1] - 1
        G[A].add(B)
        G[B].add(A)

    used = [0] * N
    dfs(0)
    if sum(used) != N:
        ans += 1

print(ans)
