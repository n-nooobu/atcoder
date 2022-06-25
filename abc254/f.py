import io
import sys

# input here
_INPUT = """\
3 5
3 5 2
8 1 3
1 2 2 3
1 3 1 3
1 1 1 1
2 2 2 2
3 3 1 1

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cumA = [0] + list(itertools.accumulate(A))
cumB = [0] + list(itertools.accumulate(B))

for q in range(Q):
    h1, h2, w1, w2 = map(int, input().split())
    h1 -= 1
    h2 -= 1
    w1 -= 1
    w2 -= 1

    s = (cumA[h2 + 1] - cumA[h1]) * (w2 - w1 + 1) + (cumB[w2 + 1] - cumB[w1]) * (h2 - h1 + 1)

