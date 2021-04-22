import io
import sys

# input here
_INPUT = """\
3 100
1
28 54 81

"""
sys.stdin = io.StringIO(_INPUT)



N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

def is_ok(x):
    i = 1
    s = 0
    c = 0
    while i < N + 2:
        s += A[i] - A[i - 1]

        if s >= x:
            s = 0
            c += 1
            i += 1
        else:
            i += 1

        if i == N + 1:
            if s < x:
                c -= 1
    return c >= K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(L, 0))
