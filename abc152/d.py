import io
import sys

# input here
_INPUT = """\
200000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

c = [[0] * 10 for _ in range(10)]
for i in range(1, N + 1):
    t = str(i)
    c[int(t[0])][int(t[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j] * c[j][i]

print(ans)
