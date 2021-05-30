import io
import sys

# input here
_INPUT = """\
1
1 R
2 G



"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N = int(input())

color = {'R': 0, 'G': 1, 'B': 2}
kawaisa = [[] for _ in range(3)]
for i in range(2 * N):
    a, c = input().split()
    kawaisa[color[c]].append(int(a))
R = sorted(kawaisa[0])
G = sorted(kawaisa[1])
B = sorted(kawaisa[2])

if len(R) % 2 == 0 and len(G) % 2 == 0 and len(B) % 2 == 0:
    print(0)
elif len(R) % 2 == 0:
    mi = 10 ** 17
    for g in G:
        if 0 < bisect_left(B, g) < len(B):
            t = min(abs(g - B[bisect_left(B, g)]), abs(g - B[bisect_left(B, g) - 1]))
        elif bisect_left(B, g) == 0:
            t = abs(g - B[bisect_left(B, g)])
        else:
            t = abs(g - B[bisect_left(B, g) - 1])
        mi = min(mi, t)
    print(mi)
elif len(G) % 2 == 0:
    mi = 10 ** 17
    for r in R:
        if 0 < bisect_left(B, r) < len(B):
            t = min(abs(r - B[bisect_left(B, r)]), abs(r - B[bisect_left(B, r) - 1]))
        elif bisect_left(B, r) == 0:
            t = abs(r - B[bisect_left(B, r)])
        else:
            t = abs(r - B[bisect_left(B, r) - 1])
        mi = min(mi, t)
    print(mi)
else:
    mi = 10 ** 17
    for r in R:
        if 0 < bisect_left(G, r) < len(G):
            t = min(abs(r - G[bisect_left(G, r)]), abs(r - G[bisect_left(G, r) - 1]))
        elif bisect_left(G, r) == 0:
            t = abs(r - G[bisect_left(G, r)])
        else:
            t = abs(r - G[bisect_left(G, r) - 1])
        mi = min(mi, t)
    print(mi)
