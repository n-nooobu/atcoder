import io
import sys

# input here
_INPUT = """\
483597848400000

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())

if N == 0:
    print('Yes')
elif N < 0 and math.log2(-N) <= 31:
    print('Yes')
elif N > 0 and math.log2(N) < 31:
    print('Yes')
else:
    print('No')
