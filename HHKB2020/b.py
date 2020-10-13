import io
import sys

# input here
_INPUT = """\
2 2
.#
#.

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            if i < H - 1 and S[i + 1][j] == '.':
                ans += 1
            if j < W - 1 and S[i][j + 1] == '.':
                ans += 1

print(ans)
