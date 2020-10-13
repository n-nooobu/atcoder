import io
import sys

# input here
_INPUT = """\
2 3
..#
#..

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]

mod = 10 ** 9 + 7

dots_tot = 0
h = [[0] * W for _ in range(H)]
for i in range(H):
    dots = 0
    for j in range(W):
        if S[i][j] == '.':
            dots_tot += 1
            dots += 1
        elif j != 0 or S[i][j - 1] != '#':
            h[i][j - dots: j] = [dots] * dots
            dots = 0
    if S[i][-1] != '#':
        h[i][-dots:] = [dots] * dots
        dots = 0

w = [[0] * H for _ in range(W)]
for i in range(W):
    dots = 0
    for j in range(H):
        if S[j][i] == '.':
            dots += 1
        elif j != 0 or S[j - 1][i] != '#':
            w[i][j - dots: j] = [dots] * dots
            dots = 0
    if S[-1][i] != '#':
        w[i][-dots:] = [dots] * dots
        dots = 0

ans = 0
two = [1]
for i in range(4 * 10 ** 6):
    two.append(two[-1] * 2 % mod)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ans += two[dots_tot] - two[dots_tot - (h[i][j] + w[j][i] - 1)]
            ans %= mod

print(ans)
