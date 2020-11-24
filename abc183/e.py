import io
import sys

# input here
_INPUT = """\
8 10
..........
..........
..........
..........
..........
..........
..........
..........

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

mod = 10 ** 9 + 7

naname = [[0] * W for _ in range(H)]
tate = [0] * W
ans = [[0] * W for _ in range(H)]
for i in range(H):
    yoko = 0
    for j in range(W):
        if S[i][j] == '#':
            yoko = 0
            tate[j] = 0
            naname[i][j] = 0
        else:
            if i == 0 and j == 0:
                t = 1
            elif i == 0 or j == 0:
                t = (yoko + tate[j]) % mod
            else:
                t = (yoko + tate[j] + naname[i - 1][j - 1]) % mod
            ans[i][j] = t
            yoko = (yoko + t) % mod
            tate[j] = (tate[j] + t) % mod
            if i == 0 or j == 0:
                naname[i][j] = t
            else:
                naname[i][j] = (naname[i - 1][j - 1] + t) % mod

print(ans[-1][-1] % mod)
