import io
import sys

# input here
_INPUT = """\
10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
    cut = 0
    for a in A:
        cut += (a - 1) // x
    return cut <= K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, 10**9))
