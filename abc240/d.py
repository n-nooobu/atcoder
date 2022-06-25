import io
import sys

# input here
_INPUT = """\
10
2 3 2 3 3 3 2 3 3 2

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))

s = 0
tutu = [[0, 1]]
for i in range(N):
    if a[i] == tutu[-1][0]:
        tutu[-1][1] += 1
        s += 1
    else:
        tutu.append([a[i], 1])
        s += 1
    while tutu[-1][0] == tutu[-1][1]:
        _, num = tutu.pop()
        s -= num
    print(s)
