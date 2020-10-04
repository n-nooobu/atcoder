import io
import sys

# input here
_INPUT = """\
10 20 30 40
"""
sys.stdin = io.StringIO(_INPUT)



A, B, C, D = map(int, input().split())

if A <= C:
    if B < C:
        print('No')
    else:
        print('Yes')
else:
    if D < A:
        print('No')
    else:
        print('Yes')
