import io
import sys

# input here
_INPUT = """\
2
1
2 0
1
1 0

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
A = []
xy = []
for _ in range(N):
    a = int(input())
    A.append(a)
    xy.append([list(map(int, input().split())) for _ in range(a)])

ans = 0
for i in itertools.product([0, 1], repeat=N):
    flag = True
    for j in range(N):
        if i[j]:
            for k in range(len(xy[j])):
                if i[xy[j][k][0] - 1] != xy[j][k][1]:
                    flag = False
    if flag:
        ans = max(ans, sum(i))

print(ans)
