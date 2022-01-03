import io
import sys

# input here
_INPUT = """\
5 5
.....
.....
.....
.....
.....

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

H, W = map(int, input().split())
C = [input() for _ in range(H)]

ans = 0
q = deque([[0, 0, 1]])
visit = [[0] * W for _ in range(H)]
while q:
    h, w, d = q.pop()
    if visit[h][w]:
        continue
    visit[h][w] = 1
    ans = max(ans, d)
    if h < H - 1:
        if C[h + 1][w] == '.':
            q.append([h + 1, w, d + 1])
    if w < W - 1:
        if C[h][w + 1] == '.':
            q.append([h, w + 1, d + 1])

print(ans)
