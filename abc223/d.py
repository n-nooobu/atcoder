import io
import sys

# input here
_INPUT = """\
4 3
2 1
3 4
2 4

"""
sys.stdin = io.StringIO(_INPUT)



import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

seen = [False] * (N + 1)
G0 = [[] for _ in range(N + 1)]
G1 = [[] for _ in range(N + 1)]
for i in range(M):
    A = AB[i][0]
    B = AB[i][1]
    G0[A].append(B)
    G1[B].append(A)
    seen[A] = True
    seen[B] = True

l = []
lseen = [False] * (N + 1)
for i in range(1, N + 1):
    if not seen[i]:
        l.append(i)
        lseen[i] = True
    if G0[i] and not G1[i]:
        l.append(i)
        lseen[i] = True

heapq.heapify(l)

ans = []
seen = [False] * (N + 1)
while l:
    p = heapq.heappop(l)
    lseen[p] = False
    flag = True
    for g1 in G1[p]:
        if not seen[g1]:
            flag = False
    if flag:
        ans.append(p)
        seen[p] = True
        for g0 in G0[p]:
            if not lseen[g0]:
                heapq.heappush(l, g0)
                lseen[g0] = True

if len(ans) == N:
    print(*ans, sep=' ')
else:
    print(-1)
