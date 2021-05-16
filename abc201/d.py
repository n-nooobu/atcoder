import io
import sys

# input here
_INPUT = """\
2 7
++-+-++
-+-+--+
"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
A = [input() for _ in range(H)]
a = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == '+':
            a[i][j] = 1
        else:
            a[i][j] = -1
h_hen = [[0, 0] for i in range(H)]
h0, h1 = 0, 0
for i in range(1, H):
    if i % 2:
        h0 += a[i][0]
    else:
        h1 += a[i][0]
    h_hen[i] = [h0, h1]
w_hen = [[0, 0] for i in range(W)]
w0, w1 = 0, 0
for i in range(1, W):
    if i % 2:
        w0 += a[0][i]
    else:
        w1 += a[0][i]
    w_hen[i] = [w0, w1]

h = H - 1
w = W - 1
p0, p1 = 0, 0
while h != 0 or w != 0:
    if (h + w) % 2 == 0:
        p1 += a[h][w]
    else:
        p0 += a[h][w]

    if h == 0:
        w -= 1
        continue
    if w == 0:
        h -= 1
        continue

    if h == 1:
        if (h + w) % 2 == 0:
            if p0 + w_hen[w][0] > p1 + w_hen[w][1]:
                print('Takahashi')
                exit()
            else:
                w -= 1
                continue
        else:
            if p0 + w_hen[w][0] < p1 + w_hen[w][1]:
                print('Aoki')
                exit()
            else:
                w -= 1
                continue

    if w == 1:
        if (h + w) % 2 == 0:
            if p0 + h_hen[h][0] > p1 + h_hen[h][1]:
                print('Takahashi')
                exit()
            else:
                h -= 1
                continue
        else:
            if p0 + h_hen[h][0] < p1 + h_hen[h][1]:
                print('Aoki')
                exit()
            else:
                h -= 1
                continue

    if a[h - 1][w] < a[h][w - 1]:
        w -= 1
    elif a[h - 1][w] > a[h][w - 1]:
        h -= 1
    else:
        if a[h - 2][w] + a[h - 1][w - 1] == -2:
            h -= 1
        else:
            w -= 1

if p0 > p1:
    print('Takahashi')
elif p0 < p1:
    print('Aoki')
else:
    print('Draw')
