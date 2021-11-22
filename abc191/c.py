import io
import sys

# input here
_INPUT = """\
5 5
.....
.###.
.###.
.###.
.....

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for h in range(H - 1):
    for w in range(W - 1):
        cnt = 0
        if S[h][w] == '#': cnt += 1
        if S[h + 1][w] == '#': cnt += 1
        if S[h][w + 1] == '#': cnt += 1
        if S[h + 1][w + 1] == '#': cnt += 1
        if cnt % 2:
            ans += 1

print(ans)
