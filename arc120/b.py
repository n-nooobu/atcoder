import io
import sys

# input here
_INPUT = """\
2 2
B.
.R
"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]
mod = 998244353

flag = [2] * (H + W - 1)
for h in range(H):
    for w in range(W):
        if S[h][w] == 'R':
            if flag[h + w] == 2:
                flag[h + w] = 1
            elif flag[h + w] == -1:
                flag[h + w] = 0
        elif S[h][w] == 'B':
            if flag[h + w] == 2:
                flag[h + w] = -1
            elif flag[h + w] == 1:
                flag[h + w] = 0

ans = 1
for i in range(H + W - 1):
    ans = (ans * abs(flag[i])) % mod

print(ans)
