import io
import sys

# input here
_INPUT = """\
8
1 2
2 3
2 4
2 5
4 7
5 6
6 8

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
G = defaultdict(set)
for i in range(N - 1):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    G[A].add(B)
    G[B].add(A)

K = 0
for i in range(N - 1):
    K = max(K, len(G[i]))

seen = [True]
