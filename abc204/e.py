import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



import math
from heapq import heappush, heappop

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(N):
    a, b, c, d = map(int, input().split())
    G[a].append([b, c, d])
    G[b].append([a, c, d])

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
