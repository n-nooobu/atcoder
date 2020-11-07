import io
import sys

# input here
_INPUT = """\
3 2 5
1 2 3
2 3 3
2
3 2
1 3


"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict, deque

N, M, L = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    A = (ABC[i][0], ABC[i][2])
    B = (ABC[i][1], ABC[i][2])
    G[ABC[i][0]].add(B)
    G[ABC[i][1]].add(A)
Q = int(input())
st = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    s = st[i][0]
    t = st[i][1]
    seen = [-1] * (N + 1)
    q = deque([])
    seen[s] = 0
    q.append([s, 0])
    while q:
        t = q.pop()
        for j in G[t[0]]:
            if seen[j[0]] > -1:
                continue
            q.append([j[0]], t[1] + j[1])
            seen[j[0]] = t[1] + j[1]

