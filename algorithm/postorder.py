import io
import sys

# input here
_INPUT = """\
11 15
0 1
1 2
2 3
3 0
0 4
4 5
5 6
6 4
5 7
7 5
8 3
8 9
9 10
10 4
10 8
"""
sys.stdin = io.StringIO(_INPUT)

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


def postorder(G, root=0):
    n = len(G)
    t_out = [None] * n
    t = 0
    dq = deque([~root, root])
    visited = [0] * n

    while dq:
        v = dq.pop()

        if v >= 0:
            # 行きがけ
            if visited[v]:
                continue
            for w in reversed(G[v]):
                if visited[w]:
                    continue
                dq.append(~w)
                dq.append(w)
            visited[v] = 1
        else:
            # 帰りがけ
            t_out[~v] = t
            t += 1

    return t_out

t_out = postorder(G, 0)
