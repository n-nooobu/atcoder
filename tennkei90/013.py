import io
import sys

# input here
_INPUT = """\
4 3
1 2 314
1 3 159
1 4 265


"""
sys.stdin = io.StringIO(_INPUT)



from heapq import heappush, heappop

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for i in range(M):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    C = ab[i][2]
    G[A].append([B, C])
    G[B].append([A, C])
INF = 10 ** 9

def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
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

dist1 = dijkstra(0, N)
distN = dijkstra(N - 1, N)
for i in range(N):
    print(dist1[i] + distN[i])
