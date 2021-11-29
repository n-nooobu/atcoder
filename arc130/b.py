import io
import sys

# input here
_INPUT = """\
1000000000 1000000000 3 5
1 1 2
1 2 2
1 3 2
1 4 2
1 5 2

"""
sys.stdin = io.StringIO(_INPUT)



H, W, C, Q = map(int, input().split())
tnc = [list(map(int, input().split())) for _ in range(Q)]

h = [0] * H
w = [0] * W
cnth = 0
cntw = 0
ans = [0] * C
for t, n, c in reversed(tnc):
    if t == 1:
        if h[n - 1]:
            continue
        h[n - 1] = 1
        ans[c - 1] += W - cntw
        cnth += 1
    else:
        if w[n - 1]:
            continue
        w[n - 1] = 1
        ans[c - 1] += H - cnth
        cntw += 1

print(*ans, sep=' ')
