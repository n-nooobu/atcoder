import io
import sys

# input here
_INPUT = """\
10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def is_ok(x):
    s = set()
    for a in A:
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    for i in s:
        for j in s:
            for k in s:
                if i | j | k == 31:
                    return True
    return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10 ** 9 + 1, 0))
