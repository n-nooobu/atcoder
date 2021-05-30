import io
import sys

# input here
_INPUT = """\
7
1 1 2 2 4 2
4
1 2
7 2
4 1
5 5


"""
sys.stdin = io.StringIO(_INPUT)



import sys
from bisect import *

N = int(input())
P = [0, 0] + list(map(int, input().split()))
Q = int(input())
UD = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    a = i
    b = P[i]
    G[a].append(b)
    G[b].append(a)

depth = [[] for _ in range(N + 1)]
num_iki = 1
num_kaeri = 1
seen = [False] * (N + 1)
seen[1] = True
iki = [0] * (N + 1)
kaeri = [0] * (N + 1)

sys.setrecursionlimit(10 ** 8)
def dfs(v, d):
    global num_iki, num_kaeri
    iki[v] = num_iki
    depth[d].append(num_iki)
    for w in G[v]:
        if seen[w]:
            continue
        seen[w] = True
        num_iki += 1
        num_kaeri += 1
        dfs(w, d + 1)
    kaeri[v] = num_kaeri

dfs(1, 0)

for i in range(Q):
    low = bisect_left(depth[UD[i][1]], iki[UD[i][0]])
    high = bisect_left(depth[UD[i][1]], kaeri[UD[i][0]])
    if high < len(depth[UD[i][1]]) and depth[UD[i][1]][high] == kaeri[UD[i][0]]:
        print(high - low + 1)
    else:
        print(high - low)
