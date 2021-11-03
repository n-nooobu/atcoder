import io
import sys

# input here
_INPUT = """\
3
1 1
2 1
1 2

"""
sys.stdin = io.StringIO(_INPUT)



from functools import cmp_to_key

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

def cmp(a, b):
    if a[1] * (b[0] - 1) == b[1] * (a[0] - 1): return 0
    return -1 if a[1] * (b[0] - 1) < b[1] * (a[0] - 1) else 1
xy = sorted(xy, key=cmp_to_key(cmp))

ans = 0
now = [10 ** 10, 0]
for i, [x, y] in enumerate(xy):
    if now[1] * x <= now[0] * (y - 1):
        ans += 1
        now = [x - 1, y]

print(ans)
