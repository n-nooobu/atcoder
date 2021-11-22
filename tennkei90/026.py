import io
import sys

# input here
_INPUT = """\
6
1 2
2 3
3 4
3 5
3 6
"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for _ in range(N)]
for i in range(N - 1):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A].append(B)
    G[B].append(A)


def dfs(s, k):
    dq = deque([s])
    while dq:
        u = dq.pop()
        flag = True
        if out[u]:
            flag = False
        for v in G[u]:
            if out[v]:
                flag = False
            if used[v]:
                continue
            used[v] = 1
            dq.append(v)
        if flag:
            out[u] = 1
            print(u + 1, end=' ')
            k += 1
            if k == N // 2:
                sys.exit()


used = [0] * N
out = [0] * N
k = 0
for i in range(N):
    if len(G[i]) == 1:
        print(i + 1, end=' ')
        out[i] = 1
        k += 1
        if k == N // 2:
            sys.exit()
dfs(0, k)
