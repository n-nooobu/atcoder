import io
import sys

# input here
_INPUT = """\
5 4 4
1 2 2
2 3 2
3 4 3
4 5 2
20
2 1
3 1
4 1
5 1
1 2
3 2
4 2
5 2
1 3
2 3
4 3
5 3
1 4
2 4
3 4
5 4
1 5
2 5
3 5
4 5

"""
sys.stdin = io.StringIO(_INPUT)



N, M, L = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
st = [list(map(int, input().split())) for _ in range(Q)]

INF = 10 ** 14
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    dist[ABC[i][0]][ABC[i][1]] = ABC[i][2]
    dist[ABC[i][1]][ABC[i][0]] = ABC[i][2]
for i in range(N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

dist2 = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] <= L:
            dist2[i][j] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist2[i][j] = min(dist2[i][j], dist2[i][k] + dist2[k][j])

for i in range(Q):
    ans = dist2[st[i][0]][st[i][1]] - 1
    if ans > 10 ** 12:
        print(-1)
    else:
        print(dist2[st[i][0]][st[i][1]] - 1)
