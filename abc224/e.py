import io
import sys

# input here
_INPUT = """\
3 3 7
1 1 4
1 2 7
2 1 3
2 3 5
3 1 2
3 2 5
3 3 5

"""
sys.stdin = io.StringIO(_INPUT)



H, W, N = map(int, input().split())
rca = [list(map(int, input().split())) for _ in range(N)]

h = [[] for _ in range(H)]
w = [[] for _ in range(W)]
for i in range(N):
    h[rca[i][0] - 1].append([rca[i][2], rca[i][0] - 1, rca[i][1] - 1])
    w[rca[i][1] - 1].append([rca[i][2], rca[i][0] - 1, rca[i][1] - 1])
for i in range(len(h)):
    h[i] = sorted(h[i])
for i in range(len(w)):
    w[i] = sorted(w[i])

s_list = []
for i in range(len(h)):
    if h[i][-1][0] == w[h[i][-1][2]][-1][0]:
        s_list.append(h[i][-1])
