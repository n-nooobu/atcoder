import io
import sys

# input here
_INPUT = """\
2 3
0 1 1
1 0 1
1 4 0
1 2
3 3

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

l = [[] for _ in range(3)]
for i in range(3):
    for color in range(C):
        t = 0
        for m in range(N):
            for n in range(N):
                if (m + n) % 3 == i:
                    t += D[c[m][n] - 1][color]
        l[i].append([t, color])
    l[i] = sorted(l[i])

ans = 10 ** 7
for i in itertools.product(range(C), repeat=3):
    if l[0][i[0]][1] == l[1][i[1]][1] or l[1][i[1]][1] == l[2][i[2]][1] or l[2][i[2]][1] == l[0][i[0]][1]:
        continue
    ans = min(ans, l[0][i[0]][0] + l[1][i[1]][0] + l[2][i[2]][0])

print(ans)
