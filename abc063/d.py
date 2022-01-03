import io
import sys

# input here
_INPUT = """\
5 2 1
900000000
900000000
1000000000
1000000000
1000000000

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, A, B = map(int, input().split())
h = sorted([int(input()) for _ in range(N)])

def is_ok(x):
    big_idx = bisect_right(h, B * x)
    cnt = 0
    for i in range(big_idx, len(h)):
        health = h[i] - B * x
        cnt = cnt + health // (A - B) + 1 if h[i] % (A - B) else cnt + health // (A - B)
    return cnt <= x

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, 10 ** 9 + 1))
