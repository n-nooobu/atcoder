import io
import sys

# input here
_INPUT = """\
5
10
10
10
10
10
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
h = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(1)
    exit()

start = 0
if h[0] < h[1]:
    state = 1
elif h[0] > h[1]:
    state = -1
else:
    state = 0

ans = 0
for i in range(1, N - 1):
    if state == 1:
        if h[i] > h[i+1]:
            state = -1
        elif h[i] == h[i+1]:
            state = 0
            ans = max(ans, i - start + 1)
            start = i + 1
    elif state == -1:
        if h[i] < h[i+1]:
            state = 1
            ans = max(ans, i - start + 1)
            start = i
        elif h[i] == h[i+1]:
            state = 0
            ans = max(ans, i - start + 1)
            start = i + 1
    elif state == 0:
        if h[i] < h[i + 1]:
            state = 1
        elif h[i] > h[i + 1]:
            state = -1
        else:
            start = i + 1

ans = max(ans, N - start)

print(ans)
