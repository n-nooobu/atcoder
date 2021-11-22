import io
import sys

# input here
_INPUT = """\
4 3
1 1 3 4

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
    return sum([min(A[i], x) for i in range(N)]) >= x * K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10 ** 18, 0))
