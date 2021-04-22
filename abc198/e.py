import io
import sys

# input here
_INPUT = """\
6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5


"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
from heapq import heappush, heappop

N = int(input())
C = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N - 1)]
G = defaultdict(set)
for i in range(N - 1):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A].add(B)
    G[B].add(A)

INF = 10 ** 9
ans = []
def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [[0, s, 0]]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済かどうか
    while hq:
        v, c = heappop(hq)[1:]  # 重み最小のノードをpopする
        seen[v] = True  # ノードを確定させる
        if not c & 1 << C[v]:
            ans.append(v)
        for w in G[v]:  # ノードvに隣接しているノードwに対して
            if seen[w]:
                continue
            if dist[v] + 1 >= dist[w]:
                continue
            dist[w] = dist[v] + 1
            heappush(hq, [dist[w], w, c | 1 << C[v]])
    return dist

dijkstra(0, N)
ans = sorted(ans)
for i in ans:
    print(i + 1)
