import io
import sys

# input here
_INPUT = """\
0 0 1

"""
sys.stdin = io.StringIO(_INPUT)



import math

X, Y, R = map(float, input().split())

ans = 0
for i in range(math.ceil(X - R), math.floor(X + R) + 1):
    p = math.sqrt(R ** 2 - (X - i) ** 2)
    ans += math.floor(Y + p) - math.ceil(Y - p) + 1

print(ans)
