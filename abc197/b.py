import io
import sys

# input here
_INPUT = """\
5 5 4 2
.#..#
#.###
##...
#..#.
#.###

"""
sys.stdin = io.StringIO(_INPUT)



H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [input() for _ in range(H)]

ans = 1
for i in reversed(range(Y)):
    if S[X][i] == '#':
        break
    ans += 1
for i in range(Y + 1, W):
    if S[X][i] == '#':
        break
    ans += 1
for i in reversed(range(X)):
    if S[i][Y] == '#':
        break
    ans += 1
for i in range(X + 1, H):
    if S[i][Y] == '#':
        break
    ans += 1

print(ans)
