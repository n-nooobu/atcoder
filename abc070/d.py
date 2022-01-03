import io
import sys

# input here
_INPUT = """\
10
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000
6 7 1000000000
7 8 1000000000
8 9 1000000000
9 10 1000000000
1 1
9 10

"""
sys.stdin = io.StringIO(_INPUT)



import math
from heapq import heappush, heappop

N = int(input())
abc = [list(map(int, input().split())) for _ in range(N - 1)]
Q, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N)]
for idx in range(N - 1):
    A = abc[idx][0] - 1
    B = abc[idx][1] - 1
    C = abc[idx][2]
    G[A].append([B, C])
    G[B].append([A, C])


def dijkstra(s, n):  # (始点, ノード数)
    dist = [math.inf] * n
    hq = [[0, s]]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済かどうか
    while hq:
        v = heappop(hq)[1]  # 重み最小のノードをpopする
        seen[v] = True  # ノードを確定させる
        for w, cost in G[v]:  # ノードvに隣接しているノードwに対して
            if seen[w]:
                continue
            if dist[v] + cost >= dist[w]:
                continue
            dist[w] = dist[v] + cost
            heappush(hq, [dist[w], w])
    return dist

dist = dijkstra(K - 1, N)
for i in range(Q):
    print(dist[xy[i][0] - 1] + dist[xy[i][1] - 1])
