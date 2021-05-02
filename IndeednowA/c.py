import io
import sys

# input here
_INPUT = """\
4
0
0
0
0
1
0

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N = int(input())
s = []
for i in range(N):
    t = int(input())
    if t > 0:
        s.append(t)
s = sorted(s)
Q = int(input())

def is_ok(x, k):
    c = len(s) - bisect_left(s, x)
    return c <= k

def meguru_bisect(ng, ok, k):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, k):
            ok = mid
        else:
            ng = mid
    return ok

for i in range(Q):
    k = int(input())
    print(meguru_bisect(-1, 10 ** 6 + 1, k))
