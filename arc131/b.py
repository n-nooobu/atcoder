import io
import sys

# input here
_INPUT = """\
1 1
.

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        l = [0] * 5
        if c[i][j] != '.':
            continue
        if i > 0:
            l[int(c[i - 1][j]) - 1] = 1
        if j > 0:
            l[int(c[i][j - 1]) - 1] = 1
        if i < H - 1:
            if c[i + 1][j] != '.':
                l[int(c[i + 1][j]) - 1] = 1
        if j < W - 1:
            if c[i][j + 1] != '.':
                l[int(c[i][j + 1]) - 1] = 1
        for k in range(5):
            if l[k] == 0:
                c[i][j] = str(k + 1)
                break

for i in range(H):
    print(*c[i], sep='')
