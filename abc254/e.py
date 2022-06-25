import io
import sys

# input here
_INPUT = """\
6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for idx in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = int(input())

used = [0] * (N + 1)
for q in range(Q):
    x, k = map(int, input().split())

    dq = deque([[x, 0]])
    used[x] = 1
    cnt = x
    visited_list = [x]
    while dq:
        u, d = dq.popleft()
        if d + 1 > k:
            continue
        for v in G[u]:
            if used[v]:
                continue
            cnt += v
            used[v] = 1
            dq.append([v, d + 1])
            visited_list.append(v)

    print(cnt)

    for v in visited_list:
        used[v] = 0
