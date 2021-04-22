import io
import sys

# input here
_INPUT = """\
2 2 4
1 1 10
2 1 20
2 2 5
1 1 30

"""
sys.stdin = io.StringIO(_INPUT)



from collections import OrderedDict
from bisect import *

N, M, Q = map(int, input().split())
TXY = [list(map(int, input().split())) for _ in range(Q)]

A = OrderedDict()
B = OrderedDict()
for i in range(N):
    A[str(i)] = 0
for i in range(M):
    B[str(i)] = 0

Asum = 0
Bsum = 0
sa = [0] * N
sb = [0] * M
st = 0
for q in range(Q):
    if TXY[q][0] == 1:
        Asum -= A[str(TXY[q][1] - 1)]
        A[str(TXY[q][1] - 1)] = TXY[q][2]
        Asum += TXY[q][2]
        A = OrderedDict(sorted(list(A.items()), key=lambda x: x[1]))
        t = st - sa[TXY[q][1] - 1] # + bisect_right(list(A.values())) * TXY[q][2] +
        sa[TXY[q][1] - 1] = bisect_right(list(A.values())) * TXY[q][2] + 
    else:
        Bsum -= B[str(TXY[q][1] - 1)]
        B[str(TXY[q][1] - 1)] = TXY[q][2]
        Bsum += TXY[q][2]
        B = OrderedDict(sorted(list(B.items()), key=lambda x: x[1]))
