import io
import sys

# input here
_INPUT = """\
4 8
701687787 500872619 516391519 599949380
458299111 633119409 377269575 717229869

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, K = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

def is_ok(x):
    right = 0
    for i in range(N):
        right += bisect_right(b, x // a[i])
    return right >= K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, 10 ** 18 + 1))
