import io
import sys

# input here
_INPUT = """\
6 9 2 3

"""
sys.stdin = io.StringIO(_INPUT)



import math

A, B, C, D = map(int, input().split())

if C * D <= B:
    print(-1)
else:
    print(math.ceil(A / (C * D - B)))
