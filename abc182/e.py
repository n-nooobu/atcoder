import io
import sys

# input here
_INPUT = """\
3 1 1 1
1 1
3 1
"""
sys.stdin = io.StringIO(_INPUT)



H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

S = [['.'] * W for _ in range(H)]
for i in range(N):
    S[AB[i][0] - 1][AB[i][1] - 1] = 'o'
for i in range(M):
    S[CD[i][0] - 1][CD[i][1] - 1] = '#'

h = [[0] * W for _ in range(H)]
for i in range(H):
    s = 0
    light = False
    for j in range(W):
        if S[i][j] == '#':
            if light:
                h[i][s: j] = [1] * (j - s)
                light = False
            s = j + 1
        if S[i][j] == 'o':
            light = True
        if j == W - 1:
            if light:
                h[i][s: W] = [1] * (W - s)
                light = False

w = [[0] * H for _ in range(W)]
for i in range(W):
    s = 0
    light = False
    for j in range(H):
        if S[j][i] == '#':
            if light:
                w[i][s: j] = [1] * (j - s)
                light = False
            s = j + 1
        if S[j][i] == 'o':
            light = True
        if j == H - 1:
            if light:
                w[i][s: H] = [1] * (H - s)
                light = False

ans = 0
for i in range(H):
    for j in range(W):
        if h[i][j] or w[j][i]:
            ans += 1

print(ans)
