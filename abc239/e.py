import io
import sys

# input here
_INPUT = """\
4 4
1 10 100 1000
1 2
2 3
3 4
1 4
2 3
3 2
4 1

"""
sys.stdin = io.StringIO(_INPUT)



import sys
sys.setrecursionlimit(int(1e7))

N, Q = map(int, input().split())
X = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N - 1)]
VK = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N)]
for idx in range(N - 1):
    A = AB[idx][0] - 1
    B = AB[idx][1] - 1
    G[A].append(B)
    G[B].append(A)

def dfs(u, l):
    used[u] = 1
    l = []
    for v in G[u]:
        if used[v]:
            continue
        l2 = dfs(v, l)
        l.extend(l2)
    l.append(X[u])
    l = sorted(l, reverse=True)[:20]
    nums[u] = l
    return l

used = [0] * N
nums = [[] for _ in range(N)]
dfs(0, [])

for i in range(Q):
    print(nums[VK[i][0] - 1][VK[i][1] - 1])
