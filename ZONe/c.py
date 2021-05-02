import io
import sys

# input here
_INPUT = """\
5
6 13 6 19 11
4 4 12 11 18
20 7 19 2 5
15 5 12 20 7
8 7 6 18 5

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def is_ok(x):

    return

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10 ** 9 + 1, 0))
