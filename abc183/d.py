import io
import sys

# input here
_INPUT = """\
4 10
1 3 5
2 4 4
3 10 6
2 4 1

"""
sys.stdin = io.StringIO(_INPUT)



N, W = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(N)]

s = [0] * (2 * 10 ** 5 + 1)
e = [0] * (2 * 10 ** 5 + 1)
for i in range(N):
    s[STP[i][0]] += STP[i][2]
    e[STP[i][1]] += STP[i][2]

w = 0
for i in range(len(s)):
    w -= e[i]
    w += s[i]
    if w > W:
        print('No')
        exit()

print('Yes')
