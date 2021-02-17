import io
import sys

# input here
_INPUT = """\
4 6
1 2 5
1 3 10
2 4 5
3 4 10
4 1 10
1 1 10

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict, deque

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
INF = 10 ** 9
time = [[INF] * N for _ in range(N)]
for i in range(M):
    A = ABC[i][0] - 1
    B = ABC[i][1] - 1
    G[A].add(B)
    time[A][B] = min(time[A][B], ABC[i][2])

ans = [INF] * N
for i in range(N):
    seen = [False] * N
    seen[i] = True
    q = deque([[i, 0]])
    tsum = [[INF] * N for _ in range(N)]
    while q:
        t, s = q.popleft()
        for j in G[t]:
            if j == i:
                ans[i] = min(ans[i], s + time[t][j])
                tsum[i][j] = s + time[t][j]
            if seen[j]:
                if tsum[i][j] > s + time[t][j]:
                    tsum[i][j] = s + time[t][j]
                else:
                    continue
            seen[j] = True
            q.append([j, s + time[t][j]])
            tsum[i][j] = s + time[t][j]
    if ans[i] == INF:
        ans[i] = -1
        print(ans[i])
    else:
        print(ans[i])