import io
import sys

# input here
_INPUT = """\
1 1 3
1
10000000000
2
9999999999
5000000000

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

for i in range(Q):
    xx = x[i]
    aidx = bisect_right(s, xx)
    if aidx > 0:
        asmall = s[aidx - 1]
    else:
        asmall = 0
    if aidx < len(s):
        abig = s[aidx]
    else:
        abig = 0
    bidx = bisect_right(t, xx)
    if bidx > 0:
        bsmall = t[bidx - 1]
    else:
        bsmall = 0
    if bidx < len(t):
        bbig = t[bidx]
    else:
        bbig = 0

    ans = 10 ** 12
    if abig and bbig:
        ans = min(ans, max(abig, bbig) - xx)
    if asmall and bsmall:
        ans = min(ans, xx - min(asmall, bsmall))
    if asmall and bbig:
        ans = min(ans, bbig - asmall + min(bbig - xx, xx - asmall))
    if abig and bsmall:
        ans = min(ans, abig - bsmall + min(abig - xx, xx - bsmall))

    print(ans)
