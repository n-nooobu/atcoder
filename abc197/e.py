import io
import sys

# input here
_INPUT = """\
9
5 5
-4 4
4 3
6 3
-5 5
-3 2
2 2
3 3
1 4

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
XC = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

lrs = []
col = 0
lrs = []
l, r = 0, 0
for x, c in XC:
    if c == col:
        l = min(l, x)
        r = max(r, x)
    else:
        lrs.append([l, r])
        l, r = x, x
        col = c
lrs.append([l, r])
lrs.append([0, 0])
lt, rt = 0, 0
l_pre, r_pre = 0, 0
for l, r in lrs[1:]:
    lt_ = min(lt + abs(l_pre-r) + abs(r-l), rt + abs(r_pre-r) + abs(r-l))
    rt_ = min(lt + abs(l_pre-l) + abs(l-r), rt + abs(r_pre-l) + abs(l-r))
    lt, rt = lt_, rt_
    l_pre, r_pre = l, r

print(min(lt, rt))
