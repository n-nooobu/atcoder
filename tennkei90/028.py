import io
import sys

# input here
_INPUT = """\
20
61 98 76 100
70 99 95 100
10 64 96 91
12 37 99 66
63 93 65 95
16 18 18 67
30 47 88 56
33 6 38 8
37 19 40 68
4 56 12 84
3 16 92 78
39 24 67 96
46 1 69 57
40 34 65 65
20 38 51 92
5 32 100 73
7 33 92 55
4 46 97 85
43 18 57 87
15 29 54 74

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]

tiles = [[0] * 1002 for _ in range(1002)]

for i, (lx, ly, rx, ry) in enumerate(lr):
    tiles[ly][lx] += 1
    tiles[ly][rx] -= 1
    tiles[ry][lx] -= 1
    tiles[ry][rx] += 1

for y in range(1002):
    for x in range(1002):
        tiles[y][x] += tiles[y][x - 1]

for y in range(1002):
    for x in range(1002):
        tiles[y][x] += tiles[y - 1][x]

ans = [0] * (N + 1)
for y in range(1002):
    for x in range(1002):
        ans[tiles[y][x]] += 1

for i in range(1, N + 1):
    print(ans[i])
