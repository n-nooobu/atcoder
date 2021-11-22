import io
import sys

# input here
_INPUT = """\
8 11
0 1
1 2
2 0
2 3
3 4
3 5
4 3
5 6
6 3
7 1
7 2
"""
sys.stdin = io.StringIO(_INPUT)

"""
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



from collections import deque

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
GT = [[] for _ in range(N)]
for i in range(M):
    A = ab[i][0]
    B = ab[i][1]
    G[A].append(B)
    GT[B].append(A)


def scc(G, GT):
    n = len(G)
    post = []
    t = 0
    visited = [0] * n

    for s in range(n):
        if visited[s]:
            continue
        dq = deque([~s, s])

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
                post.append(~v)
                t += 1

    visited = [0] * n
    scc_cnt = []

    for s in reversed(post):
        if visited[s]:
            continue
        dq = deque([s])
        cnt = 0

        while dq:
            v = dq.pop()
            if visited[v]:
                continue
            for w in reversed(GT[v]):
                if visited[w]:
                    continue
                dq.append(w)
            visited[v] = 1
            cnt += 1
        scc_cnt.append(cnt)

    return scc_cnt

scc_cnt = scc(G, GT)
