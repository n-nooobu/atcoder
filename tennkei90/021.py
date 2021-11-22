import io
import sys

# input here
_INPUT = """\
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter
import sys
sys.setrecursionlimit(int(1e6))

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]
for i in range(M):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    G[A].append(B)
    RG[B].append(A)


def scc():
    def dfs(u):
        used[u] = 1
        for v in G[u]:
            if not used[v]:
                dfs(v)
        postorder.append(u)

    def rdfs(u, k):
        group[u] = k
        used[u] = 1
        for v in RG[u]:
            if not used[v]:
                rdfs(v, k)

    used = [0] * N
    postorder = []
    for s in range(N):
        if not used[s]:
            dfs(s)

    used = [0] * N
    group = [-1] * N
    k = 0
    for s in reversed(postorder):
        if not used[s]:
            rdfs(s, k)
            k += 1

    return k, group


k, group = scc()
c = Counter(group)

ans = 0
for value in c.values():
    ans += value * (value - 1) // 2

print(ans)
