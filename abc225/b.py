import io
import sys

# input here
_INPUT = """\
10
9 10
3 10
4 10
8 10
1 10
2 10
7 10
6 10
5 10

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for _ in range(N + 1)]
for i in range(N - 1):
    A = ab[i][0]
    B = ab[i][1]
    G[A].append(B)
    G[B].append(A)

for v in G:
    if len(v) == N - 1:
        print('Yes')
        sys.exit()

print('No')
