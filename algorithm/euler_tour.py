import io
import sys

# input here
_INPUT = """\
15 14
0 1
1 2
1 3
0 4
4 5
5 6
5 7
4 8
8 9
8 10
0 11
11 12
11 13
13 14
"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
for i in range(M):
    A = ab[i][0]
    B = ab[i][1]
    G[A].append(B)
    G[B].append(A)


def euler_tour(G, root=0):
    n = len(G)
    euler = []
    t_in, t_out = [None] * n, [None] * n
    depth = [None] * n
    t0, t1 = 0, 0
    dq = deque([[~root, root], [root, 0]])
    dq2 = deque()
    visited = [0] * n

    while dq:
        v, d = dq.pop()

        if v >= 0:
            # 行きがけ
            euler.append(v)
            t_in[v] = t0
            t0 += 1
            depth[v] = d

            if visited[v]:
                continue
            for w in reversed(G[v]):
                if visited[w]:
                    dq.append([~w, v])
                else:
                    dq2.append([w, d + 1])

            dq.extend(dq2)
            dq2 = deque()
            visited[v] = 1
        else:
            # 帰りがけ
            if ~v != d:
                euler.append(~v)
            t_out[d] = t0
            t0 += 1

    return euler, t_in, t_out, depth


euler, t_in, t_out, depth = euler_tour(G, 0)
