import io
import sys

# input here
_INPUT = """\
4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30

"""
sys.stdin = io.StringIO(_INPUT)



from heapq import heappush, heappop

N, M = map(int, input().split())
G = [[] for _ in range(N)]
INF = 10 ** 9
exist = [[0] * N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    if exist[A - 1][B - 1]:
        if G[A - 1][exist[A - 1][B - 1] - 1][1] > C:
            G[A - 1][exist[A - 1][B - 1] - 1][1] = C
    else:
        G[A - 1].append([B - 1, C])
        exist[A - 1][B - 1] = len(G[A - 1])

def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = []  # (distance, node)
    for w, cost in G[s]:
        dist[w] = cost
        heappush(hq, [dist[w], w])
    seen = [False] * n  # ノードが確定済かどうか
    while hq:
        v = heappop(hq)[1]  # 重み最小のノードをpopする
        seen[v] = True  # ノードを確定させる
        if v == s:
            return dist
        for w, cost in G[v]:  # ノードvに隣接しているノードwに対して
            if seen[w]:
                continue
            if dist[v] + cost >= dist[w]:
                continue
            dist[w] = dist[v] + cost
            heappush(hq, [dist[w], w])
    return dist

for i in range(N):
    dist = dijkstra(i, N)
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
