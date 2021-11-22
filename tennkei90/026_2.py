import io
import sys

# input here
_INPUT = """\
2
1 2

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter, deque
import sys
sys.setrecursionlimit(int(1e6))

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for _ in range(N)]
for i in range(N - 1):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A].append(B)
    G[B].append(A)


def dfs(u, cur):
    color[u] = cur
    for v in G[u]:
        if color[v] == -1:
            dfs(v, 1 - cur)


def dfs(s):
    dq = deque([[s, 0]])
    while dq:
        u, cur = dq.pop()
        color[u] = cur
        for v in G[u]:
            if color[v] == -1:
                dq.append([v, 1 - cur])


color = [-1] * N
dfs(0)
c = Counter(color)
iro = max(c.items(), key=lambda x: x[1])[0]
ans = []
for i in range(N):
    if color[i] == iro:
        ans.append(i + 1)
print(*ans[:N//2], sep=' ')
