import io
import sys

# input here
_INPUT = """\
2 2

"""
sys.stdin = io.StringIO(_INPUT)



import math

t, N = map(int, input().split())

if N * 100 % t == 0:
    print(math.floor((N * 100 // t) * (1 + t / 100)) - 1)
else:
    print(math.floor((N * 100 // t + 1) * (1 + t / 100)) - 1)

for i in range(205):
    print(i, math.floor((100 + t) / 100 * i), (100 + t) / 100 * i)
