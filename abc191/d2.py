import io
import sys

# input here
_INPUT = """\
42782.4720 31949.0192 99999.99

"""
sys.stdin = io.StringIO(_INPUT)



import math

X, Y, R = map(float, input().split())

ans = 0
if math.ceil(X - R) == X - R:
    start = X - R + 1
else:
    start = math.ceil(X - R)
if math.floor(X + R) == X + R:
    end = X + R
else:
    end = math.floor(X + R) + 1
for i in range(start, end):
    p = math.sqrt(R ** 2 - (X - i) ** 2)
    if math.floor(Y + p) == Y + p:
        t0 = Y + p - 1
    else:
        t0 = math.floor(Y + p)
    if math.ceil(Y - p) == Y - p:
        t1 = Y - p + 1
    else:
        t1 = math.ceil(Y - p)
    ans += t0 - t1 + 1
for i in

print(ans)