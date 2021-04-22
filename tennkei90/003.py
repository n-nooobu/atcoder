import io
import sys

# input here
_INPUT = """\
31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
G = defaultdict(set)
for i in range(N-1):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A].add(B)
    G[B].add(A)

def tree_diameter(s):
    seen = [False] * N
    seen[s] = True
    q = deque([[s, 0]])
    mt = s
    md = 0
    while q:
        t, d = q.pop()
        for w in G[t]:
            if seen[w]:
                continue
            seen[w] = True
            q.append([w, d+1])
            if md < d + 1:
                mt = w
                md = d + 1
    return mt, md

print(tree_diameter(tree_diameter(0)[0])[1] + 1)
