import io
import sys

# input here
_INPUT = """\
11 10 9
"""
sys.stdin = io.StringIO(_INPUT)



A, B, N = map(int, input().split())

if N < B:
    x = N
else:
    x = B - 1

print(int(A * x / B // 1) - A * int(x / B // 1))
