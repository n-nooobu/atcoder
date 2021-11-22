import io
import sys

# input here
_INPUT = """\
5 5
00100
03040
20903
05060
00300

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
b = [list(map(int, input())) for _ in range(N)]

a = [[0] * M for _ in range(N)]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        num = min([b[i - 1][j], b[i][j - 1], b[i][j + 1], b[i + 1][j]])
        a[i][j] = num
        b[i - 1][j] -= num
        b[i][j - 1] -= num
        b[i][j + 1] -= num
        b[i + 1][j] -= num

for i in range(N):
    print(*a[i], sep='')
