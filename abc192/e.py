import io
import sys

# input here
_INPUT = """\
9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4

"""
sys.stdin = io.StringIO(_INPUT)



from heapq import heappush, heappop

N, M, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B, T, K = map(int, input().split())
    G[A - 1].append([B - 1, T, K])
    G[B - 1].append([A - 1, T, K])

INF = 10 ** 15
dist = [INF] * N
hq = [[0, X - 1]]  # (distance, node)
dist[X - 1] = 0
seen = [False] * N  # ノードが確定済かどうか
while hq:
    d, v = heappop(hq)  # 重み最小のノードをpopする
    seen[v] = True  # ノードを確定させる
    for w, t, k in G[v]:  # ノードvに隣接しているノードwに対して
        if seen[w]:
            continue
        if d % k == 0:
            cost = t
        else:
            cost = t + (d // k + 1) * k - d
        if d + cost >= dist[w]:
            continue
        dist[w] = d + cost
        heappush(hq, [dist[w], w])

if dist[Y - 1] == INF:
    print(-1)
else:
    print(dist[Y - 1])
