import io
import sys

# input here
_INPUT = """\
1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)



A, B, C, K = map(int, input().split())

if K <= A:
    print(K)
elif K <= A + B:
    print(A)
else:
    print(A - (K - (A + B)))
