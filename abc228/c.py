import io
import sys

# input here
_INPUT = """\
4 2
127 235 78
192 134 298
28 56 42
96 120 250

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

Psum = [sum(P[i]) for i in range(N)]
Psorted = sorted(Psum)

for i in range(N):
    if N - bisect_right(Psorted, Psum[i] + 300) < K:
        print('Yes')
    else:
        print('No')
